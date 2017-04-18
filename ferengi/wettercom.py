"""Wetter.com weather data import"""

from datetime import datetime, timedelta
from json import loads
from hashlib import md5

from requests import get
from peewee import Model, PrimaryKeyField, ForeignKeyField, BooleanField, \
    SmallIntegerField, CharField, DateTimeField, DecimalField, IntegerField
from peeweeplus import dec2dict

from configparserplus import ConfigParserPlus

from .api import UpToDate, APIError, ferengi_database


__all__ = ['City', 'Forecast', 'Client', 'client']

config = ConfigParserPlus('/etc/ferengi.d/wettercom.conf')
database = ferengi_database(
    config['db']['database'],
    user=config['db']['user'],
    passwd=config['db']['passwd'])


class _WeatherModel(Model):
    """Abstract, basic weather DB model"""

    class Meta:
        database = database
        schema = database.database

    id = PrimaryKeyField()


class City(_WeatherModel):
    """Available regions"""

    name = CharField(255)
    post_code = CharField(255)
    region_code = CharField(2)
    url = CharField(255)
    country = CharField(255)
    last_update = DateTimeField(null=True, default=None)
    auto_update = BooleanField(default=False)

    @classmethod
    def from_dict(cls, dictionary):
        """Creates a city from a dictionary"""
        city = cls()
        city.name = dictionary['name']
        city.post_code = dictionary['post_code']
        city.region_code = dictionary['region_code']
        city.url = dictionary['url']
        city.country = dictionary['country']
        return city

    @classmethod
    def update_all(cls, force=False):
        """Updates all cities set to be auto updated"""
        for city in cls.select().where(cls.auto_update == 1):
            city.update_forecast(force=force)

    @property
    def up2date(self):
        """Determines whether weather is up to date"""
        if self.last_update is None:
            return False
        else:
            return datetime.now() - self.last_update <= timedelta(days=1)

    def to_dict(self):
        """Converts the record to a JSON-compilant dictionary"""
        return None     # TODO: implement

    def _update_forecast(self):
        """Updates the city's weather forecast"""
        for forecast in client(self.id)['list']:
            for record in Forecast.from_dict(self, forecast):
                record.save()

    def update_forecast(self, force=False):
        """Updates the city's weather forecast"""
        if not self.up2date or force:
            return self._update_forecast()
        else:
            raise UpToDate() from None


class Forecast(_WeatherModel):
    """Regional weather forecast"""

    SUB_FORECASTS = ('06:00', '11:00', '17:00', '23:00')

    city = ForeignKeyField(City, db_column='city')
    parent = ForeignKeyField(
        'self', db_column='parent', null=True, default=None)
    timestamp = CharField(255)
    p = SmallIntegerField()
    wd = SmallIntegerField()
    w = SmallIntegerField()
    tx = SmallIntegerField()
    pc = SmallIntegerField()
    tp = DecimalField(4, 2)
    tn = SmallIntegerField()
    ws = SmallIntegerField()
    d = IntegerField()

    @classmethod
    def _from_dict(cls, city, timestamp, dictionary, parent=None):
        """Creates a forecast for the respective
        city from the specified dictionary
        """
        forecast = cls()
        forecast.city = city
        forecast.parent = parent
        forecast.timestamp = timestamp
        forecast.p = dictionary['p']
        forecast.wd = dictionary['wd']
        forecast.w = dictionary['w']
        forecast.tx = dictionary['tx']
        forecast.pc = dictionary['pc']
        forecast.tp = dictionary['tp']
        forecast.tn = dictionary['tn']
        forecast.ws = dictionary['ws']
        forecast.d = dictionary['d']
        return forecast

    @classmethod
    def from_dict(cls, city, timestamp, dictionary):
        """Creates a forecast for the respective
        city from the specified dictionary
        """
        forecast = cls._from_dict(city, timestamp, dictionary)
        yield forecast

        for sub_forecast in cls.SUB_FORECASTS:
            try:
                d = forecast[sub_forecast]
            except KeyError:
                pass
            else:
                yield cls._from_dict(city, timestamp, d, parent=forecast)

    def to_dict(self):
        """Converts the forecast into a JSON-compliant dictionary"""
        dictionary = {
            'p': self.p,
            'wd': self.wd,
            'w': self.w,
            'tx': self.tx,
            'pc': self.pc,
            'tp': dec2dict(self.tp),
            'tn': self.tn,
            'ws': self.ws,
            'd': self.d}

        if self.parent is None:
            for child in self.__class__.select().where(
                    self.__class__.parent == self):
                dictionary[child.timestamp] = child.to_dict()

        return dictionary


class Client():
    """Receive and store weather data"""

    def __init__(self, base_url=None, user_name=None, api_key=None):
        """Sets base URL and API key"""
        self.base_url = base_url or self.config['base_url']
        self.user_name = user_name or self.config['user_name']
        self.api_key = api_key or self.config['api_key']

    def __call__(self, city, raw=False):
        """Retrievels weather data for the respective city ID"""
        response = get(self.url(city))

        if raw:
            return response
        elif response.status_code == 200:
            return loads(response.text)
        else:
            raise APIError(response)

    @property
    def config(self):
        """Returns the API config section"""
        return config['api']

    def checksum(self, city):
        """Returns the API checksum"""
        hashval = self.user_name + self.api_key + city
        return md5(hashval.encode()).hexdigest()

    def url(self, city):
        """Returns the URL for the respective city"""
        return self.base_url.format(city, self.user_name, self.checksum(city))


client = Client()   # Default client
