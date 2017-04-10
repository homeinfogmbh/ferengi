"""Weather data import"""

from datetime import datetime, timedelta

from requests import get
from peewee import Model, PrimaryKeyField, ForeignKeyField, \
    SmallIntegerField, CharField, DateTimeField, DecimalField, FloatField

from peeweeplus import MySQLDatabase
from configparserplus import ConfigParserPlus


config = ConfigParserPlus('/etc/ferengi.d/weather.conf')
database = MySQLDatabase(
    config['db']['db'],
    host=config['db']['host'],
    user=config['db']['user'],
    passwd=config['db']['passwd'])


class UpToDate(Exception):
    """Indicates that the record is up to date"""

    pass


class City(Model):
    """Available regions"""

    id = PrimaryKeyField()
    name = CharField(255)
    country = CharField(2)
    longitude = FloatField()
    latitude = FloatField()
    last_update = DateTimeField(null=True, default=None)

    @classmethod
    def from_dict(cls, dictionary):
        """Creates a city from a dictionary"""
        city = cls()
        city.city_id = dictionary['_id']
        city.name = dictionary['name']
        city.country = dictionary['country']
        city.longitude = dictionary['coord']['long']
        city.latitude = dictionary['coord']['lat']
        return city

    @classmethod
    def initialize(cls, list_):
        """Initializes table from dictionary list"""
        for dictionary in list_:
            cls.from_dict(dictionary).save()

    @property
    def up2date(self):
        """Determines whether weather is up to date"""
        if self.last_update is None:
            return False
        else:
            if datetime.now() - self.last_update <= timedelta(days=1):
                return True
            else:
                return False

    def to_dict(self):
        """Converts the record to a JSON-compilant dictionary"""
        return None     # TODO: implement

    def _update_forecast(self):
        """Updates the city's weather forecast"""
        forecast = Forecast.from_dict(self, client(self.city_id))
        return forecast.save()

    def update_forecast(self, force=False):
        """Updates the city's weather forecast"""
        if not self.up2date or force:
            return self._update_forecast()
        else:
            raise UpToDate() from None


class Forecast(Model):
    """Regional weather forecast"""

    id = PrimaryKeyField()
    city = ForeignKeyField(City, db_column='region')
    dt = DateTimeField()
    temp = DecimalField(5, 2)
    temp_min = DecimalField(5, 2)
    temp_max = DecimalField(5, 2)
    pressure = DecimalField(6, 2)
    sea_level = DecimalField(6, 2)
    grd_level = DecimalField(6, 2)
    humidity = SmallIntegerField()
    temp_kf = DecimalField(4, 2)
    clouds_all = SmallIntegerField()
    wind_speed = DecimalField(4, 2)
    wind_deg = DecimalField(6, 3)

    @classmethod
    def from_dict(cls, city, dictionary):
        """Creates a forecast for the respective
        city from the specified dictionary
        """
        forecast = cls()
        forecast.city = city
        forecast.dt = datetime.fromtimestamp(dictionary['dt'])
        # TODO: implement
        return forecast


class Weather(Model):
    """Weather details"""

    id = PrimaryKeyField()
    forecast = ForeignKeyField(Forecast, db_column='forecast')
    weather_id = SmallIntegerField()
    main = CharField(255)
    description = CharField(255)
    icon = CharField(255)


class Client():
    """Receive and store weather data"""

    def __init__(self, base_url=None, api_key=None):
        """Sets base URL and API key"""
        self.base_url = base_url or config['client']['base_url']
        self.api_key = api_key or config['client']['api_key']

    def __call__(self, city_id):
        """Retrievels weather data for the respective city ID"""
        return get()    # TODO: implement


client = Client()   # Default client
