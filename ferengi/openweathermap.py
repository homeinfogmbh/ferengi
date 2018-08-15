"""Open Weather Map weather data import"""

from contextlib import suppress
from datetime import datetime, timedelta
from json import loads

from peewee import Model, ForeignKeyField, BooleanField, SmallIntegerField, \
    CharField, DateTimeField, DecimalField, FloatField
from requests import get

from configlib import INIParser
from peeweeplus import dec2dict

from ferengi.api import UpToDate, APIError, get_database
from ferengi.dom import weather as weather_dom


__all__ = [
    'UpToDate',
    'City',
    'Forecast',
    'Weather',
    'Client',
    'CLIENT']

CONFIG = INIParser('/etc/ferengi.d/openweathermap.conf')
DATABASE = get_database(CONFIG)
ICONS = {
    '01d': 22,
    '02d': 13,
    '04d': 12,
    '03d': 5,
    '50d': 8,
    'Nebel mit Reifbildung': 5,
    'Sprühregen': 15,
    'leichter Sprühregen': 17,
    'starker Sprühregen': 15,
    'leichter Sprühregen, gefrierend': 17,
    'starker Sprühregen, gefrierend': 15,
    '10d': 15,
    'leichter Regen': 2,
    'mäßiger Regen': 17,
    'starker Regen': 15,
    'leichter Regen, gefrierend': 2,
    'mäßiger od. starker Regen, gefrierend': 17,
    'leichter Schnee-Regen': 16,
    'starker Schnee-Regen': 16,
    '13d': 20,
    'leichter Schneefall': 20,
    'mäßiger Schneefall': 20,
    'starker Schneefall': 20,
    'Schauer': 2,
    'leichter Regen - Schauer': 2,
    'Regen - Schauer': 2,
    '09d': 4,
    'leichter Schnee / Regen - Schauer': 18,
    'starker Schnee / Regen - Schauer': 18,
    'leichter Schnee - Schauer': 3,
    'mäßiger od. starker Schnee - Schauer': 20,
    '11d': 1,
    'leichtes Gewitter': 1,
    'starkes Gewitter': 1,
    'k.A.': 6}


def _day_dom(forecasts):
    """Converts a set of forecasts of the same day to DOM."""

    day_forecast = weather_dom.DayForecast()

    for forecast in forecasts:
        for weather in forecast.weather:
            day_forecast.icon_id = ICONS.get(weather.icon)

            if day_forecast.icon_id is not None:
                day_forecast.weather_text = weather.description
                break

        temp_min = int(forecast.temp_min)

        if day_forecast.tempmin is None or day_forecast.tempmin > temp_min:
            day_forecast.tempmin = temp_min

        temp_max = int(forecast.temp_max)

        if day_forecast.tempmax is None or day_forecast.tempmax < temp_max:
            day_forecast.tempmax = temp_max

        dt_ = forecast.dt

        if day_forecast.dtmin is None or day_forecast.dtmin > dt_:
            day_forecast.dtmin = dt_

        if day_forecast.dt is None or day_forecast.dt < dt_:
            day_forecast.dt = dt_

    return day_forecast


def forecasts_to_dom(city, forecasts):
    """Converts the forecasts to today's DOM."""

    now = datetime.now()
    today = now.date()
    tomorrow = today + timedelta(days=1)
    day_after_tomorrow = tomorrow + timedelta(days=1)
    today_forecasts = []
    tomorrow_forecasts = []
    day_after_tomorrow_forecasts = []

    for forecast in forecasts:
        forecast_date = forecast.dt.date()

        if forecast_date == today:
            today_forecasts.append(forecast)
        elif forecast_date == tomorrow:
            tomorrow_forecasts.append(forecast)
        elif forecast_date == day_after_tomorrow:
            day_after_tomorrow_forecasts.append(forecast)

    xml = weather_dom.xml()
    forecast = weather_dom.Forecast()
    forecast.day.append(_day_dom(today_forecasts))
    forecast.day.append(_day_dom(tomorrow_forecasts))
    forecast.day.append(_day_dom(day_after_tomorrow_forecasts))
    xml.forecast = forecast
    xml.name = city
    xml.pubdate = now.strftime('%Y-%m-%d %H:%M:%S')
    return xml


class _WeatherModel(Model):
    """Abstract, basic weather DB model."""

    class Meta:
        database = DATABASE
        schema = DATABASE.database


class City(_WeatherModel):
    """Available regions."""

    name = CharField(255)
    country = CharField(2)
    longitude = FloatField()
    latitude = FloatField()
    last_update = DateTimeField(null=True)
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

        return datetime.now() - self.last_update <= timedelta(days=1)

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
        for forecast in CLIENT(self.id)['list']:
            for record in Forecast.from_dict(self, forecast):
                record.save()

    def update_forecast(self, force=False):
        """Updates the city's weather forecast."""
        if not self.up2date or force:
            old_forecasts = tuple(self.forecasts)
            self._update_forecast()

            for old_forecast in old_forecasts:
                old_forecast.delete_instance()

            self.last_update = datetime.now()
            self.save()
        else:
            raise UpToDate() from None


class Forecast(_WeatherModel):
    """Regional weather forecast."""

    city = ForeignKeyField(City, column_name='city', backref='forecasts')
    dt = DateTimeField()
    temp = DecimalField(4, 2, null=True)
    temp_min = DecimalField(4, 2, null=True)
    temp_max = DecimalField(4, 2, null=True)
    pressure = DecimalField(6, 2, null=True)
    sea_level = DecimalField(6, 2, null=True)
    grnd_level = DecimalField(6, 2, null=True)
    humidity = SmallIntegerField(null=True)
    clouds_all = SmallIntegerField(null=True)
    wind_speed = DecimalField(4, 2, null=True)
    wind_deg = DecimalField(6, 3, null=True)
    rain_3h = DecimalField(6, 3, null=True)
    snow_3h = DecimalField(6, 3, null=True)

    @classmethod
    def by_city(cls, city, since=None, until=None):
        """Yields forecases of the specified
        city within the specified time period.
        """
        if isinstance(city, str):
            city = City.get(City.name == city)

        expression = cls.city == city

        if since is not None:
            expression &= cls.dt >= since

        if until is not None:
            expression &= cls.dt < until

        return cls.select().where(expression)

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

        weather = [weather.to_dict() for weather in self.weather]

        if weather:
            dictionary['weather'] = weather

        return dictionary


class Weather(_WeatherModel):
    """Weather details."""

    forecast = ForeignKeyField(
        Forecast, column_name='forecast', backref='weather',
        on_delete='CASCADE')
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


class Client:
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

        if response.status_code == 200:
            return loads(response.text)

        raise APIError(response)

    @property
    def config(self):
        """Returns the API config section."""
        return CONFIG['api']


CLIENT = Client(units='metric', lang='de')   # Default client.
