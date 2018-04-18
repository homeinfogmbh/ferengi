"""ORM models for the garbage disposal module."""

from datetime import datetime
from time import sleep

from peewee import Model, PrimaryKeyField, ForeignKeyField, CharField, \
    DateTimeField, DateField, BooleanField
from requests.exceptions import ConnectionError

from homeinfo.crm import Address
from terminallib import Terminal

from ferengi.garbage_disposal.config import LOGGER, INTERVAL, DISTRICTS, \
    WAIT_TIME, DATABASE
from ferengi.garbage_disposal.exceptions import NoInformation
from ferengi.garbage_disposal.interface import get_disposals

__all__ = ['create_tables', 'Location']


def create_tables():
    """Creates the respective tables."""

    for table in (Location, Pickup, PickupDate):
        table.create_table()


class _GarbageDisposalModel(Model):
    """Base Model."""

    class Meta:
        database = DATABASE
        schema = DATABASE.database

    id = PrimaryKeyField()


class Location(_GarbageDisposalModel):
    """Garbage disposal model."""

    address = ForeignKeyField(Address, column_name='address')
    code = CharField(32)
    street = CharField(64)
    house_number = CharField(32)
    district = CharField(64)
    timestamp = DateTimeField(default=datetime.now)

    @classmethod
    def up2date(cls, address):
        """Determines whether the respective address' data is up to date."""
        garbage_disposals = tuple(cls.by_address(address))

        if not garbage_disposals:
            return False

        return all(garbage_disposal.timestamp + INTERVAL >= datetime.now()
                   for garbage_disposal in garbage_disposals)

    @classmethod
    def by_address(cls, address):
        """Returns the respective garbage disposal by address."""
        return cls.select().where(cls.address == address)

    @classmethod
    def refresh(cls, address, force=False):
        """Updates the records for the respective address."""
        if force or not cls.up2date(address):
            cls.purge(address)

            for record in cls.from_address(address):
                record.save()

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
        for record in cls.select().where(cls.address == address):
            record.delete_instance()

    @classmethod
    def from_address(cls, address):
        """Creates an entry from the respective address."""
        for pickup_solution in get_disposals(address):
            yield from cls.from_dict(address, pickup_solution.to_dict())

    @classmethod
    def from_dict(cls, address, dictionary):
        """Creates the respective records from the given dictionary."""
        record = cls()
        record.address = address
        record.code = dictionary['code']
        record.street = dictionary['street']
        record.house_number = dictionary['house_number']
        record.district = dictionary['district']
        yield record

        for pickup in dictionary['pickups']:
            yield from Pickup.from_dict(record, pickup)

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        return {
            'code': self.code,
            'street': self.street,
            'house_number': self.house_number,
            'district': self.district,
            'pickups': [pickup.to_dict() for pickup in self.pickups]}


class Pickup(_GarbageDisposalModel):
    """A garbage pickup."""

    location = ForeignKeyField(
        Location, column_name='location', on_delete='CASCADE')
    type_ = CharField(32)
    image_link = CharField(255)
    weekday = CharField(32)
    interval = CharField(16)

    @classmethod
    def from_dict(cls, location, dictionary):
        """Creates and yields respective records from the dictionary."""
        record = cls()
        record.location = location
        record.type_ = dictionary['type']
        record.image_link = dictionary['image_link']
        record.weekday = dictionary['weekday']
        record.interval = dictionary['interval']
        yield record

        for date in dictionary.get('next_dates', ()):
            yield PickupDate.from_dict(record, date)

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        return {
            'type': self.type_,
            'image_link': self.image_link,
            'weekday': self.weekday,
            'interval': self.interval,
            'next_dates': [date.to_dict() for date in self.next_dates]}


class PickupDate(_GarbageDisposalModel):
    """A pickup date."""

    pickup = ForeignKeyField(
        Pickup, column_name='pickup', backref='next_dates',
        on_delete='CASCADE')
    date = DateField()
    weekday = CharField(16)
    exceptional = BooleanField()

    @classmethod
    def from_dict(cls, pickup, dictionary):
        """Creates and yields respective records from the dictionary."""
        record = cls()
        record.pickup = pickup
        record.date = datetime.strptime(dictionary['date'], '%Y-%m-%d')
        record.weekday = dictionary['weekday']
        record.exceptional = dictionary['exceptional']
        return record

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'weekday': self.weekday,
            'exceptional': self.exceptional}
