"""ORM models for the garbage disposal module."""

from datetime import datetime
from time import sleep
from typing import Iterable, Iterator

from peewee import BooleanField
from peewee import CharField
from peewee import DateField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import Model
from requests.exceptions import ConnectionError     # pylint: disable=W0622

from hwdb import Deployment
from mdb import Address

from ferengi.garbage_disposal.config import DATABASE
from ferengi.garbage_disposal.config import DISTRICTS
from ferengi.garbage_disposal.config import INTERVAL
from ferengi.garbage_disposal.config import LOGGER
from ferengi.garbage_disposal.config import WAIT_TIME
from ferengi.garbage_disposal.exceptions import NoInformation
from ferengi.garbage_disposal.interface import get_disposals


__all__ = ['create_tables', 'Location']


def create_tables():
    """Creates the respective tables."""

    for table in (Location, Pickup, PickupDate):
        table.create_table()


class _GarbageDisposalModel(Model):
    """Base Model."""

    class Meta:     # pylint: disable=C0111,R0903
        database = DATABASE
        schema = DATABASE.database


class Location(_GarbageDisposalModel):
    """Garbage disposal model."""

    address = ForeignKeyField(Address, column_name='address')
    code = CharField(32)
    street = CharField(64)
    house_number = CharField(32)
    district = CharField(64)
    timestamp = DateTimeField(default=datetime.now)

    @classmethod
    def up2date(cls, address: Address) -> bool:
        """Determines whether the respective address' data is up to date."""
        garbage_disposals = tuple(cls.by_address(address))

        if not garbage_disposals:
            return False

        return all(garbage_disposal.timestamp + INTERVAL >= datetime.now()
                   for garbage_disposal in garbage_disposals)

    @classmethod
    def by_address(cls, address: Address) -> Iterable[Location]:
        """Returns the respective garbage disposal by address."""
        return cls.select().where(cls.address == address)

    @classmethod
    def refresh(cls, address: Address, force: bool = False):
        """Updates the records for the respective address."""
        if force or not cls.up2date(address):
            cls.purge(address)

            for record in cls.from_address(address):
                record.save()

    @classmethod
    def refresh_all(cls, addresses: Iterable[Address], force: bool = False):
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
    def update_all(cls, force: bool = False):
        """Updates the garbage disposal for all active systems."""
        addresses = set()

        for deployment in Deployment.select().where(Deployment.testing == 0):
            addresses.add(deployment.address)

        cls.refresh_all(addresses, force=force)

    @classmethod
    def purge(cls, address: Address):
        """Purges records for the respective address."""
        for record in cls.select().where(cls.address == address):
            record.delete_instance()

    @classmethod
    def from_address(cls, address: Address) -> Iterator[Location]:
        """Creates an entry from the respective address."""
        for pickup_solution in get_disposals(address):
            yield from cls.from_dict(address, pickup_solution.to_json())

    @classmethod
    def from_dict(cls, address: Address, dct: dict) -> Iterator[Model]:
        """Creates the respective records from the given dictionary."""
        record = cls()
        record.address = address
        record.code = dct['code']
        record.street = dct['street']
        record.house_number = dct['house_number']
        record.district = dct['district']
        yield record

        for pickup in dct['pickups']:
            yield from Pickup.from_dict(record, pickup)

    def to_json(self) -> dict:
        """Returns a JSON-ish dictionary."""
        return {
            'code': self.code,
            'street': self.street,
            'house_number': self.house_number,
            'district': self.district,
            'pickups': [pickup.to_json() for pickup in self.pickups]
        }


class Pickup(_GarbageDisposalModel):
    """A garbage pickup."""

    location = ForeignKeyField(
        Location, column_name='location', backref='pickups',
        on_delete='CASCADE')
    type_ = CharField(32)
    image_link = CharField(255)
    weekday = CharField(32)
    interval = CharField(16)

    @classmethod
    def from_dict(cls, location: Location, dct: dict) -> Iterator[Model]:
        """Creates and yields respective records from the dictionary."""
        record = cls()
        record.location = location
        record.type_ = dct['type']
        record.image_link = dct['image_link']
        record.weekday = dct['weekday']
        record.interval = dct['interval']
        yield record

        for date in dct.get('next_dates', ()):
            yield PickupDate.from_dict(record, date)

    def to_json(self) -> dict:
        """Returns a JSON-ish dictionary."""
        return {
            'type': self.type_,
            'image_link': self.image_link,
            'weekday': self.weekday,
            'interval': self.interval,
            'next_dates': [date.to_json() for date in self.next_dates]
        }


class PickupDate(_GarbageDisposalModel):
    """A pickup date."""

    pickup = ForeignKeyField(
        Pickup, column_name='pickup', backref='next_dates',
        on_delete='CASCADE')
    date = DateField()
    weekday = CharField(16)
    exceptional = BooleanField()

    @classmethod
    def from_dict(cls, pickup: Pickup, dct: dict) -> PickupDate:
        """Creates and yields respective records from the dictionary."""
        record = cls()
        record.pickup = pickup
        record.date = datetime.strptime(dct['date'], '%Y-%m-%d')
        record.weekday = dct['weekday']
        record.exceptional = dct['exceptional']
        return record

    def to_json(self) -> dict:
        """Returns a JSON-ish dictionary."""
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'weekday': self.weekday,
            'exceptional': self.exceptional
        }
