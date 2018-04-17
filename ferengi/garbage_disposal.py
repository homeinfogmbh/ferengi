"""Garbage disposal data."""

from datetime import datetime, timedelta
from logging import getLogger

from peewee import Model, PrimaryKeyField, ForeignKeyField, BooleanField, \
    CharField, DateField, DateTimeField

from aha import LocationNotFound, AhaDisposalClient
from configlib import INIParser
from homeinfo.crm import Address
from terminallib import Terminal

from ferengi.api import get_database


CONFIG = INIParser('/etc/ferengi.d/garbage_disposal.conf')
DATABASE = get_database(CONFIG)
LOGGER = getLogger(__file__)

try:
    INTERVAL = CONFIG['api']['interval']
except KeyError:
    INTERVAL = 24
else:
    INTERVAL = int(INTERVAL)

try:
    DISTRICTS = CONFIG['api']['districts']
except KeyError:
    DISTRICTS = ['Hannover']
else:
    DISTRICTS = DISTRICTS.split()


INTERVAL = timedelta(hours=INTERVAL)


class NoInformation(Exception):
    """Indicates that no pickup information is available."""

    pass


def get_dispsal(address):
    """Returns the respective disposal dictionary."""

    aha_client = AhaDisposalClient(district=address.city or 'Hannover')

    try:
        pickup_information = aha_client.by_address(
            address.street, address.house_number)
    except LocationNotFound as location_not_found:
        LOGGER.warning('Location not found: %s.', location_not_found)
        raise NoInformation()

    if pickup_information is None:
        LOGGER.warning('No disposal information for address: %s.', address)
        raise NoInformation()

    return pickup_information.to_dict()


class _GarbageDisposalModel(Model):
    """Base Model."""

    class Meta:
        database = DATABASE
        schema = DATABASE.database

    id = PrimaryKeyField()


class Location(_GarbageDisposalModel):
    """Represents loading locations."""

    type_ = CharField(7)
    code = CharField(16)
    street = CharField(32)
    house_number = CharField(8)
    district = CharField(32, null=True)

    @classmethod
    def from_dict(cls, type_, dictionary):
        """Yields respective records."""
        record = cls()
        record.type_ = type_
        record.code = dictionary['code']
        record.street = dictionary['street']
        record.house_number = dictionary['house_number']
        record.district = dictionary['district']
        return record

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        return {
            'code': self.code,
            'street': self.street,
            'house_number': self.house_number,
            'district': self.district}


class GarbageDisposal(_GarbageDisposalModel):
    """Garbage disposal model."""

    location = ForeignKeyField(Address, column_name='location')
    loading_location = ForeignKeyField(
        Location, null=True, column_name='loading_location')
    pickup_location = ForeignKeyField(
        Location, null=True, column_name='pickup_location')
    timestamp = DateTimeField(default=datetime.now)

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

        if 'loading_location' in dictionary:
            location = Location.from_dict(
                'loading', dictionary['loading_location'])
            record.loading_location = location
            yield location
        elif 'pickup_location' in dictionary:
            location = Location.from_dict(
                'pickup', dictionary['pickup_location'])
            record.pickup_location = location
            yield location

        yield record

        for pickup in dictionary.get('pickups', ()):
            yield from Pickup.from_dict(record, pickup)

    def delete_instance(self, recursive=False, delete_nullable=False):
        """Deletes this record."""
        rel_records = []

        if self.loading_location is not None:
            rel_records.append(self.loading_location)

        if self.pickup_location is not None:
            rel_records.append(self.pickup_location)

        result = super().delete_instance(
            recursive=recursive, delete_nullable=delete_nullable)

        for rel_record in rel_records:
            rel_record.delete_instance()

        return result

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        dictionary = {'pickups': [pickup.to_dict() for pickup in self.pickups]}

        if self.loading_location is not None:
            dictionary['loading_location'] = self.loading_location.to_dict()

        if self.pickup_location is not None:
            dictionary['pickup_location'] = self.pickup_location.to_dict()

        return dictionary


class Pickup(_GarbageDisposalModel):
    """Represents a pickup."""

    garbage_disposal = ForeignKeyField(
        GarbageDisposal, column_name='garbage_disposal', backref='pickups',
        on_delete='CASCADE')
    type_ = CharField(32)
    weekday = CharField(32)
    interval = CharField(16)
    image_link = CharField(255)

    @classmethod
    def from_dict(cls, garbage_disposal, dictionary):
        """Yields the respective models."""
        record = cls()
        record.garbage_disposal = garbage_disposal
        record.type_ = dictionary['type']
        record.weekday = dictionary['weekday']
        record.interval = dictionary['interval']
        record.image_link = dictionary['image_link']
        yield record

        for next_date in dictionary.get('next_dates', ()):
            yield PickupDate.from_dict(record, next_date)

    def to_dict(self):
        """Returns a JSON-ish dictionary."""
        return {
            'type': self.type_,
            'weekday': self.weekday,
            'interval': self.interval,
            'image_link': self.image_link,
            'next_dates': [date.to_dict() for date in self.next_dates]}


class PickupDate(_GarbageDisposalModel):
    """Represents the next collection dates."""

    pickup = ForeignKeyField(
        Pickup, column_name='pickup', backref='next_dates',
        on_delete='CASCADE')
    date = DateField()
    weekday = CharField(2)
    exceptional = BooleanField()

    @classmethod
    def from_dict(cls, pickup, dictionary):
        """Returns the respective record."""
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
