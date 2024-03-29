"""WGSI application to retrieve weather data."""

from datetime import date
from typing import Union

from wsgilib import ACCEPT, JSON, XML

from ferengi.openweathermap.functions import forecasts_to_dom
from ferengi.openweathermap.orm import City, Forecast


__all__ = ["ROUTES"]


def get_weather(city: City) -> Union[tuple[str, int], JSON, XML]:
    """Returns the respective weather forecasts."""

    try:
        forecasts = Forecast.by_city(city, since=date.today())
    except City.DoesNotExist:
        return "No such city.", 404

    forecasts = tuple(forecasts)

    if not forecasts:
        return f"No forecasts for {city}.", 404

    if "application/xml" in ACCEPT or "*/*" in ACCEPT:
        return XML(forecasts_to_dom(city, forecasts))

    if "application/json" in ACCEPT:
        return JSON([forecast.to_json() for forecast in forecasts])

    return "Invalid content type.", 406


ROUTES = [("GET", "/weather/<city>", get_weather)]
