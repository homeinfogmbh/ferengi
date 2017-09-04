"""Open Weather Map weather data import"""

from datetime import datetime, timedelta
from contextlib import suppress
from json import loads

from requests import get
from peewee import Model, PrimaryKeyField, ForeignKeyField, BooleanField, \
    SmallIntegerField, CharField, DateTimeField, DecimalField, FloatField
from peeweeplus import dec2dict

from configparserplus import ConfigParserPlus

from .api import UpToDate, APIError, ferengi_database

__all__ = [
    'config',
    'database',
    'UpToDate',
    'City',
    'Forecast',
    'Weather',
    'Client',
    'client']

config = ConfigParserPlus('/etc/ferengi.d/openweathermap.conf')
database = ferengi_database(
    config['db']['database'],
    user=config['db']['user'],
    passwd=config['db']['passwd'])


class _WeatherModel(Model):
    """Abstract, basic weather DB model."""

    class Meta:
        database = database
        schema = database.database

    id = PrimaryKeyField()


class City(_WeatherModel):
    """Available regions."""

    name = CharField(255)
    country = CharField(2)
    longitude = FloatField()
    latitude = FloatField()
    last_update = DateTimeField(null=True, default=None)
    auto_update = BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def from_dict(cls, dictionary):
        """Creates a city from a dictionary."""
        city = cls()
        city.id = dictionary['_id']
        city.name = dictionary['name']
        city.country = dictionary['country']
        city.longitude = dictionary['coord']['lon']
        city.latitude = dictionary['coord']['lat']
        return city

    @classmethod
    def initialize(cls, list_):
        """Initializes table from dictionary list."""
        for dictionary in list_:
            cls.from_dict(dictionary).save()

    @classmethod
    def update_all(cls, force=False):
        """Updates all cities set to be auto updated."""
        for city in cls.select().where(cls.auto_update == 1):
            try:
                city.update_forecast(force=force)
            except UpToDate:
                print('Forecast for {} is already up-to-date.'.format(city))
            else:
                print('Updated forecast for {}.'.format(city))

    @property
    def up2date(self):
        """Determines whether weather is up to date."""
        if self.last_update is None:
            return False
        else:
            return datetime.now() - self.last_update <= timedelta(days=1)

    @property
    def forecasts(self):
        """Yields the current forecasts for this city."""
        return Forecast.select().where(Forecast.city == self)

    def to_dict(self):
        """Converts the record to a JSON-compilant dictionary."""
        dictionary = {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'auto_update': self.auto_update}

        if self.last_update is not None:
            dictionary['last_update'] = self.last_update.isoformat()

        return dictionary

    def _update_forecast(self):
        """Updates the city's weather forecast."""
        for forecast in client(self.id)['list']:
            for record in Forecast.from_dict(self, forecast):
                record.save()

    def update_forecast(self, force=False):
        """Updates the city's weather forecast."""
        if not self.up2date or force:
            old_forecasts = tuple(self.forecasts)
            self._update_forecast()

            for old_forecast in old_forecasts:
                old_forecast.remove()

            self.last_update = datetime.now()
            self.save()
        else:
            raise UpToDate() from None


class Forecast(_WeatherModel):
    """Regional weather forecast."""

    city = ForeignKeyField(City, db_column='city')
    dt = DateTimeField()
    temp = DecimalField(4, 2, null=True, default=None)
    temp_min = DecimalField(4, 2, null=True, default=None)
    temp_max = DecimalField(4, 2, null=True, default=None)
    pressure = DecimalField(6, 2, null=True, default=None)
    sea_level = DecimalField(6, 2, null=True, default=None)
    grnd_level = DecimalField(6, 2, null=True, default=None)
    humidity = SmallIntegerField(null=True, default=None)
    clouds_all = SmallIntegerField(null=True, default=None)
    wind_speed = DecimalField(4, 2, null=True, default=None)
    wind_deg = DecimalField(6, 3, null=True, default=None)
    rain_3h = DecimalField(6, 3, null=True, default=None)
    snow_3h = DecimalField(6, 3, null=True, default=None)

    @classmethod
    def from_dict(cls, city, dictionary):
        """Creates a forecast for the respective
        city from the specified dictionary.
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
            forecast.rain_3h = dictionary['rain']['3h']

        with suppress(KeyError):
            forecast.snow_3h = dictionary['snow']['3h']

        yield forecast

        for weather in dictionary['weather']:
            yield Weather.from_dict(forecast, weather)

    def to_dict(self):
        """Converts the forecast into a JSON-compliant dictionary."""
        dictionary = {'dt': self.dt.isoformat()}
        main = {}

        if self.temp is not None:
            main['temp'] = dec2dict(self.temp)

        if self.temp_min is not None:
            main['temp_min'] = dec2dict(self.temp_min)

        if self.temp_max is not None:
            main['temp_max'] = dec2dict(self.temp_max)

        if self.pressure is not None:
            main['pressure'] = dec2dict(self.pressure)

        if self.sea_level is not None:
            main['sea_level'] = dec2dict(self.sea_level)

        if self.grnd_level is not None:
            main['grnd_level'] = dec2dict(self.grnd_level)

        if self.humidity is not None:
            main['humidity'] = self.humidity

        if main:
            dictionary['main'] = main

        if self.clouds_all is not None:
            dictionary['clouds'] = {'all': self.clouds_all}

        wind = {}

        if self.wind_speed is not None:
            wind['speed'] = dec2dict(self.wind_speed)

        if self.wind_deg is not None:
            wind['deg'] = dec2dict(self.wind_deg)

        if wind:
            dictionary['wind'] = wind

        if self.rain_3h is not None:
            dictionary['rain'] = {'3h': dec2dict(self.rain_3h)}

        if self.snow_3h is not None:
            dictionary['snow'] = {'3h': dec2dict(self.snow_3h)}

        weather = [weather.to_dict() for weather in Weather.select().where(
            Weather.forecast == self)]

        if weather:
            dictionary['weather'] = weather

        return dictionary

    def remove(self):
        """Removes this forecast."""
        for weather in Weather.select().where(Weather.forecast == self):
            weather.delete_instance()

        self.delete_instance()


class Weather(_WeatherModel):
    """Weather details."""

    forecast = ForeignKeyField(Forecast, db_column='forecast')
    weather_id = SmallIntegerField()
    main = CharField(255)
    description = CharField(255)
    icon = CharField(255)

    @classmethod
    def from_dict(cls, forecast, dictionary):
        """Creates a weather record for the respective
        forecast from the specified dictionary.
        """
        weather = cls()
        weather.forecast = forecast
        weather.weather_id = dictionary['id']
        weather.main = dictionary['main']
        weather.description = dictionary['description']
        weather.icon = dictionary['icon']
        return weather

    def to_dict(self):
        """Converts the weather into a JSON-compliant dictionary."""
        return {
            'id': self.weather_id,
            'main': self.main,
            'description': self.description,
            'icon': self.icon}


class Client():
    """Receive and store weather data."""

    def __init__(self, base_url=None, api_key=None, **params):
        """Sets base URL and API key"""
        self.base_url = base_url or self.config['base_url']
        self.api_key = api_key or self.config['api_key']
        self.params = params

    def __call__(self, city_id, raw=False):
        """Retrievels weather data for the respective city ID."""
        self.params.update(
            {'id': city_id, 'appid': self.api_key})
        response = get(self.base_url, params=self.params)

        if raw:
            return response
        elif response.status_code == 200:
            print(response.text)
            return loads(response.text)

        raise APIError(response)

    @property
    def config(self):
        """Returns the API config section."""
        return config['api']


client = Client(units='metric', lang='de')   # Default client
