"""Weather data import"""

from datetime import datetime, timedelta
from contextlib import suppress
from json import loads

from requests import get
from peewee import Model, PrimaryKeyField, ForeignKeyField, IntegerField, \
    SmallIntegerField, CharField, DateTimeField, DecimalField, FloatField, \
    BooleanField

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


class _WeatherModel(Model):
    """Abstract, basic weather DB model"""

    class Meta:
        database = database
        schema = database.database

    id = PrimaryKeyField()


class City(_WeatherModel):
    """Available regions"""

    name = CharField(255)
    country = CharField(2)
    longitude = FloatField()
    latitude = FloatField()
    last_update = DateTimeField(null=True, default=None)
    auto_update = BooleanField(default=False)

    @classmethod
    def from_dict(cls, dictionary):
        """Creates a city from a dictionary"""
        city = cls()
        city.id = dictionary['_id']
        city.name = dictionary['name']
        city.country = dictionary['country']
        city.longitude = dictionary['coord']['lon']
        city.latitude = dictionary['coord']['lat']
        return city

    @classmethod
    def initialize(cls, list_):
        """Initializes table from dictionary list"""
        for dictionary in list_:
            cls.from_dict(dictionary).save()

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

    city = ForeignKeyField(City, db_column='city')
    dt = DateTimeField()
    temp = SmallIntegerField(null=True, default=None)
    temp_min = SmallIntegerField(null=True, default=None)
    temp_max = SmallIntegerField(null=True, default=None)
    pressure = SmallIntegerField(null=True, default=None)
    sea_level = SmallIntegerField(null=True, default=None)
    grnd_level = SmallIntegerField(null=True, default=None)
    humidity = SmallIntegerField(null=True, default=None)
    clouds_all = SmallIntegerField(null=True, default=None)
    wind_speed = DecimalField(4, 2, null=True, default=None)
    wind_deg = DecimalField(6, 3, null=True, default=None)
    rain_3h = DecimalField(6, 3, null=True, default=None)
    snow_3h = DecimalField(6, 3, null=True, default=None)

    @classmethod
    def from_dict(cls, city, dictionary):
        """Creates a forecast for the respective
        city from the specified dictionary
        """
        forecast = cls()
        forecast.city = city
        forecast.dt = datetime.fromtimestamp(dictionary['dt'])

        with suppress(KeyError):
            forecast.temp = dictionary['main']['temp']

        with suppress(KeyError):
            forecast.temp_min = dictionary['main']['temp_min']

        with suppress(KeyError):
            forecast.temp_max = dictionary['main']['temp_max']

        with suppress(KeyError):
            forecast.pressure = dictionary['main']['pressure']

        with suppress(KeyError):
            forecast.sea_level = dictionary['main']['sea_level']

        with suppress(KeyError):
            forecast.grnd_level = dictionary['main']['grnd_level']

        with suppress(KeyError):
            forecast.humidity = dictionary['main']['humidity']

        with suppress(KeyError):
            forecast.clouds_all = dictionary['clouds']['all']

        with suppress(KeyError):
            forecast.wind_speed = dictionary['wind']['speed']

        with suppress(KeyError):
            forecast.wind_deg = dictionary['wind']['deg']

        with suppress(KeyError):
            forecast.clouds_all = dictionary['clouds']['all']

        with suppress(KeyError):
            forecast.rain_3h = dictionary['rain']['3h']

        with suppress(KeyError):
            forecast.snow_3h = dictionary['snow']['3h']

        yield forecast

        for weather in dictionary['weather']:
            yield Weather.from_dict(forecast, weather)


class Weather(_WeatherModel):
    """Weather details"""

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
        params = {'id': city_id, 'appid': self.api_key, 'units': 'metric'}
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
