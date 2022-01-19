"""Open Weather Map weather data import"""

from __future__ import annotations
from contextlib import suppress
from datetime import datetime, timedelta
from typing import Iterator, List

from peewee import CharField
from peewee import DateTimeField
from peewee import DecimalField
from peewee import FloatField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import ModelSelect
from peewee import SmallIntegerField

from peeweeplus import MySQLDatabaseProxy, dec2dict

from ferengi.api import UpToDate
from ferengi.openweathermap.config import CONFIG
from ferengi.openweathermap.client import CLIENT


__all__ = ['City', 'Forecast', 'Weather']


DATABASE = MySQLDatabaseProxy('ferengi_openweathermap',
                              'ferengi.d/openweathermap.conf')


class WeatherModel(Model):
    """Abstract, basic weather DB model."""

    class Meta:     # pylint: disable=C0111,R0903
        database = DATABASE
        schema = DATABASE.database


class City(WeatherModel):
    """Available regions."""

    id = IntegerField(primary_key=True)     # pylint: disable=C0103
    name = CharField(255)
    country = CharField(2)
    longitude = FloatField()
    latitude = FloatField()
    last_update = DateTimeField(null=True)

    def __str__(self):
        return self.name

    @classmethod
    def from_json(cls, json: dict) -> City:
        """Creates a city from a dict."""
        city = cls()
        city.id = json['_id']
        city.name = json['name']
        city.country = json['country']
        city.longitude = json['coord']['lon']
        city.latitude = json['coord']['lat']
        return city

    @classmethod
    def initialize(cls, json: List[dict]):
        """Initializes table from dictionary list."""
        for city in json:
            cls.from_json(city).save()

    @property
    def up2date(self) -> bool:
        """Determines whether weather is up to date."""
        if self.last_update is None:
            return False

        return datetime.now() - self.last_update <= timedelta(days=1)

    def to_json(self) -> dict:
        """Converts the record to a JSON-ish dictionary."""
        dictionary = {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

        if self.last_update is not None:
            dictionary['last_update'] = self.last_update.isoformat()

        return dictionary

    def _update_forecast(self) -> None:
        """Updates the city's weather forecast."""
        for forecast in CLIENT(self.id)['list']:
            for record in Forecast.from_json(forecast, city=self):
                record.save()

    def update_forecast(self, force=False) -> None:
        """Updates the city's weather forecast."""
        if not self.up2date or force:
            old_forecasts = tuple(self.forecasts)   # pylint: disable=E1101
            self._update_forecast()

            for old_forecast in old_forecasts:
                old_forecast.delete_instance()

            self.last_update = datetime.now()
            self.save()
        else:
            raise UpToDate() from None


class Forecast(WeatherModel):  # pylint: disable=R0902
    """Regional weather forecast."""

    city = ForeignKeyField(
        City, column_name='city', backref='forecasts', lazy_load=False)
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
    def by_city(cls, city: City, since: datetime = None,
                until: datetime = None) -> ModelSelect:
        """Yields forecasts of the specified
        city within the specified time period.
        """
        if isinstance(city, str):
            countries = CONFIG['config']['countries'].split()
            city = City.get((City.name == city) & (City.country << countries))

        expression = cls.city == city

        if since is not None:
            expression &= cls.dt >= since

        if until is not None:
            expression &= cls.dt < until

        return cls.select().where(expression)

    @classmethod
    def from_json(cls, json: dict, *, city: City) -> Iterator[WeatherModel]:
        """Creates a forecast for the respective
        city from the specified dict.
        """
        forecast = cls(city=city)
        forecast.dt = datetime.fromtimestamp(json['dt'])

        with suppress(KeyError):
            forecast.temp = json['main']['temp']

        with suppress(KeyError):
            forecast.temp_min = json['main']['temp_min']

        with suppress(KeyError):
            forecast.temp_max = json['main']['temp_max']

        with suppress(KeyError):
            forecast.pressure = json['main']['pressure']

        with suppress(KeyError):
            forecast.sea_level = json['main']['sea_level']

        with suppress(KeyError):
            forecast.grnd_level = json['main']['grnd_level']

        with suppress(KeyError):
            forecast.humidity = json['main']['humidity']

        with suppress(KeyError):
            forecast.clouds_all = json['clouds']['all']

        with suppress(KeyError):
            forecast.wind_speed = json['wind']['speed']

        with suppress(KeyError):
            forecast.wind_deg = json['wind']['deg']

        with suppress(KeyError):
            forecast.rain_3h = json['rain']['3h']

        with suppress(KeyError):
            forecast.snow_3h = json['snow']['3h']

        yield forecast

        for weather in json['weather']:
            yield Weather.from_json(weather, forecast=forecast)

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects forecasts."""
        if not cascade:
            return super().select(*args, **kwargs)

        return super().select(*{cls, City, *args}, **kwargs).join(City)

    def to_json(self) -> dict:  # pylint: disable=R0912
        """Converts the forecast into a JSON-ish dict."""
        json = {'dt': self.dt.isoformat()}
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
            json['main'] = main

        if self.clouds_all is not None:
            json['clouds'] = {'all': self.clouds_all}

        wind = {}

        if self.wind_speed is not None:
            wind['speed'] = dec2dict(self.wind_speed)

        if self.wind_deg is not None:
            wind['deg'] = dec2dict(self.wind_deg)

        if wind:
            json['wind'] = wind

        if self.rain_3h is not None:
            json['rain'] = {'3h': dec2dict(self.rain_3h)}

        if self.snow_3h is not None:
            json['snow'] = {'3h': dec2dict(self.snow_3h)}

        weather = [weather.to_json() for weather in self.weather]

        if weather:
            json['weather'] = weather

        return json


class Weather(WeatherModel):
    """Weather details."""

    forecast = ForeignKeyField(
        Forecast, column_name='forecast', backref='weather',
        on_delete='CASCADE', lazy_load=False)
    weather_id = SmallIntegerField()
    main = CharField(255)
    description = CharField(255)
    icon = CharField(255)

    @classmethod
    def from_json(cls, json: dict, *, forecast: Forecast) -> Weather:
        """Creates a weather record for the respective
        forecast from the specified dict.
        """
        weather = cls(forecast=forecast)
        weather.weather_id = json['id']
        weather.main = json['main']
        weather.description = json['description']
        weather.icon = json['icon']
        return weather

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects weather."""
        if not cascade:
            return super().select(*args, **kwargs)

        return super().select(*{cls, Forecast, City, *args}, **kwargs).join(
            Forecast).join(City)

    def to_json(self) -> dict:
        """Converts the weather into a JSON-ish dict."""
        return {
            'id': self.weather_id,
            'main': self.main,
            'description': self.description,
            'icon': self.icon
        }
