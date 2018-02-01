"""WSGI services."""

from datetime import datetime
from json import dumps

from flask import Response, Flask

from ferengi.openweathermap import City, Forecast

__all__ = ['APPLICATION']

APPLICATION = Flask('ferengi')


@APPLICATION.route('/weather/<city>')
def get_weather(city):
    """Returns the respective weather forecasts."""
    try:
        city = City.get(City.name == city)
    except City.DoesNotExist:
        return ('No such city.', 404)

    forecasts = [
        forecast.to_dict() for forecast in Forecast.select().where(
            (Forecast.city == city) &
            (Forecast.dt >= datetime.now()))]
    return Response(dumps(forecasts), mimetype='application/json')
