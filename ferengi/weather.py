"""Weather data import"""

from datetime import datetime, timedelta
from contextlib import suppress
from json import loads

from requests import get
from peewee import Model, PrimaryKeyField, ForeignKeyField, \
    SmallIntegerField, CharField, DateTimeField, DecimalField, FloatField

from configparserplus import ConfigParserPlus

from .api import ferengi_database

__all__ = [
    'config',
    'database',
    'UpToDate',
    'APIError',
    'City',
    'Forecast',
    'Weather',
    'Client',
    'client']

config = ConfigParserPlus('/etc/ferengi.d/weather.conf')
database = ferengi_database(
    config['db']['database'],
    user=config['db']['user'],
    passwd=config['db']['passwd'])


class UpToDate(Exception):
    """Indicates that the record is up to date"""

    pass


class APIError(Exception):
    """Indicates that data could not be received from the API"""

    def __init__(self, response):
        """Sets status code and response text"""
        super().__init__(response.text)
        self.response = response

    def __int__(self):
        """Returns the status code"""
        return self.response.status_code

    def __str__(self):
        """Returns the response text"""
        return self.response.text


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
        for record in Forecast.from_dict(self, client(self.city_id)):
            record.save()

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
    clouds_all = SmallIntegerField()
    wind_speed = DecimalField(4, 2)
    wind_deg = DecimalField(6, 3)
    rain_3h = DecimalField(5, 3, null=True, default=None)
    snow_3h = DecimalField(5, 3, null=True, default=None)

    @classmethod
    def from_dict(cls, city, dictionary):
        """Creates a forecast for the respective
        city from the specified dictionary
        """
        forecast = cls()
        forecast.city = city
        forecast.dt = datetime.fromtimestamp(dictionary['dt'])
        forecast.temp = dictionary['main']['temp']
        forecast.temp_min = dictionary['main']['temp_min']
        forecast.temp_max = dictionary['main']['temp_max']
        forecast.pressure = dictionary['main']['pressure']
        forecast.sea_level = dictionary['main']['sea_level']
        forecast.grd_level = dictionary['main']['grd_level']
        forecast.humidity = dictionary['main']['humidity']
        forecast.clouds_all = dictionary['clouds']['all']
        forecast.wind_speed = dictionary['wind']['speed']
        forecast.wind_deg = dictionary['wind']['deg']
        forecast.clouds_all = dictionary['clouds']['all']

        with suppress(AttributeError):
            forecast.rain_3h = dictionary['rain']['3h']

        with suppress(AttributeError):
            forecast.snow_3h = dictionary['snow']['3h']

        yield forecast

        for weather in dictionary['weather']:
            yield Weather.from_dict(forecast, weather)


class Weather(Model):
    """Weather details"""

    id = PrimaryKeyField()
    forecast = ForeignKeyField(Forecast, db_column='forecast')
    weather_id = SmallIntegerField()
    main = CharField(255)
    description = CharField(255)
    icon = CharField(255)

    @classmethod
    def from_dict(cls, forecast, dictionary):
        """Creates a weather record for the respective
        forecast from the specified dictionary
        """
        weather = cls()
        weather.forecast = forecast
        weather.weather_id = dictionary['id']
        weather.main = dictionary['main']
        weather.description = dictionary['description']
        weather.icon = dictionary['icon']
        return weather


class Client():
    """Receive and store weather data"""

    def __init__(self, base_url=None, api_key=None):
        """Sets base URL and API key"""
        self.base_url = base_url or self.config['base_url']
        self.api_key = api_key or self.config['api_key']

    def __call__(self, city_id, raw=False):
        """Retrievels weather data for the respective city ID"""
        params = {'id': city_id, 'appid': self.api_key}
        response = get(self.base_url, params=params)

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


client = Client()   # Default client
