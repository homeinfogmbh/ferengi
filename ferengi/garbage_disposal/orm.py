"""ORM models for the garbage disposal module."""

from datetime import datetime
from json import loads, dumps
from time import sleep

from peewee import Model, PrimaryKeyField, ForeignKeyField, TextField, \
    DateTimeField
from requests.exceptions import ConnectionError

from homeinfo.crm import Address
from terminallib import Terminal

from ferengi.garbage_disposal.config import LOGGER, INTERVAL, DISTRICTS, \
    WAIT_TIME, DATABASE
from ferengi.garbage_disposal.exceptions import NoInformation
from ferengi.garbage_disposal.interface import get_dispsal


class _GarbageDisposalModel(Model):
    """Base Model."""

    class Meta:
        database = DATABASE
        schema = DATABASE.database

    id = PrimaryKeyField()


class GarbageDisposal(_GarbageDisposalModel):
    """Garbage disposal model."""

    location = ForeignKeyField(Address, column_name='location')
    timestamp = DateTimeField(default=datetime.now)
    json = TextField()

    @classmethod
    def by_address(cls, address):
        """Returns the respective garbage disposal by address."""
        return cls.get(cls.location == address)

    @classmethod
    def refresh(cls, address, force=False):
        """Updates the records for the respective address."""
        try:
            garbage_disposal = cls.by_address(address)
        except cls.DoesNotExist:
            up2date = False
        else:
            up2date = garbage_disposal.timestamp + INTERVAL >= datetime.now()

        if force or not up2date:
            cls.purge(address)
            record = cls.from_address(address)
            record.save()
            return record

        return None

    @classmethod
    def refresh_all(cls, addresses, force=False):
        """Refreshes all addresses."""
        for address in addresses:
            if address.city not in DISTRICTS:
                continue    # Skip non-requestsed districts.

            try:
                cls.refresh(address, force=force)
            except NoInformation:
                continue
            except ConnectionError:
                LOGGER.warning('AHA cancelled connection.')
                sleep(WAIT_TIME)

    @classmethod
    def update_all(cls, force=False):
        """Updates the garbage disposal for all active terminals."""
        addresses = set()

        for terminal in Terminal.select().where(
                (Terminal.deleted >> None) & (Terminal.testing == 0)
                & ~(Terminal.location >> None)):
            try:
                address = terminal.location.address
            except AttributeError:
                continue

            addresses.add(address)

        cls.refresh_all(addresses, force=force)

    @classmethod
    def purge(cls, address):
        """Purges records for the respective address."""
        for record in cls.select().where(cls.location == address):
            record.delete_instance()

    @classmethod
    def from_address(cls, address):
        """Creates an entry from the respective address."""
        dictionary = get_dispsal(address)
        return cls.from_dict(address, dictionary)

    @classmethod
    def from_dict(cls, address, dictionary):
        """Creates the respective records from the given dictionary."""
        record = cls()
        record.location = address
        record.json = dumps(dictionary)
        return record

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        return loads(self.json)
