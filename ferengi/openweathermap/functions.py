"""Utility functions."""

from collections import Counter
from datetime import date, datetime, timedelta
from typing import Iterable, Iterator, Optional, Tuple

from ferengi.openweathermap import dom  # pylint: disable=E0611
from ferengi.openweathermap.orm import City, Forecast


__all__ = ['forecasts_to_dom']


ICONS = {
    '01d': 22,
    '02d': 13,
    '03d': 5,
    '04d': 12,
    '09d': 4,
    '10d': 15,
    '11d': 1,
    '13d': 20,
    '50d': 8,
    '01n': 22,
    '02n': 13,
    '03n': 5,
    '04n': 12,
    '09n': 4,
    '10n': 15,
    '11n': 1,
    '13n': 20,
    '50n': 8
}


def _min_temps(forecasts: Iterable[Forecast]) -> Iterator[int]:
    """Yields minimum temperatures of forecasts."""

    for forecast in forecasts:
        if forecast.temp_min is not None:
            yield round(forecast.temp_min)


def _max_temps(forecasts: Iterable[Forecast]) -> Iterator[int]:
    """Yields maximum temperatures of forecasts."""

    for forecast in forecasts:
        if forecast.temp_max is not None:
            yield round(forecast.temp_max)


def _get_temps(forecasts: Iterable[Forecast]) -> Tuple[int, int]:
    """Returns the min and max temperature."""

    try:
        min_ = min(_min_temps(forecasts))
    except ValueError:
        min_ = None

    try:
        max_ = max(_max_temps(forecasts))
    except ValueError:
        max_ = None

    return (min_, max_)


def _get_icon_ids(forecasts: Iterable[Forecast]) -> Iterator[str]:
    """Yields translated icon IDs."""

    for forecast in forecasts:
        for weather in forecast.weather:
            yield ICONS.get(weather.icon, 6)


def _get_icon_id(forecasts: Iterable[Forecast]) -> Optional[str]:
    """Returns the most common icon ID."""

    try:
        return Counter(_get_icon_ids(forecasts)).most_common(1)[0][0]
    except IndexError:
        return None


def _get_weather_texts(forecasts: Iterable[Forecast]) -> Iterator[str]:
    """Yields weather texts."""

    for forecast in forecasts:
        for weather in forecast.weather:
            if weather.description:
                yield weather.description


def _get_weather_text(forecasts: Iterable[Forecast]) -> Optional[str]:
    """Returns the most common weather text."""

    try:
        return Counter(_get_weather_texts(forecasts)).most_common(1)[0][0]
    except IndexError:
        return None


def _day_dom(forecasts: Iterable[Forecast], date_: date) -> dom.DayForecast:
    """Converts a set of forecasts of the same day to DOM."""

    day_forecast = dom.DayForecast()
    day_forecast.tempmin, day_forecast.tempmax = _get_temps(forecasts)
    day_forecast.date = date_
    day_forecast.icon_id = _get_icon_id(forecasts)
    day_forecast.weather_text = _get_weather_text(forecasts)
    return day_forecast


def forecasts_to_dom(city: City, forecasts: Iterable[Forecast]) -> dom.xml:
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

    xml = dom.xml()
    forecast = dom.Forecast()
    forecast.day = [
        _day_dom(today_forecasts, today),
        _day_dom(tomorrow_forecasts, tomorrow),
        _day_dom(day_after_tomorrow_forecasts, day_after_tomorrow)
    ]
    xml.forecast = forecast
    xml.name = city
    xml.pubdate = now.strftime('%Y-%m-%d %H:%M:%S')
    return xml
