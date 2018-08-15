"""Utility functions."""

from datetime import datetime, timedelta

from ferengi.openweathermap import dom


__all__ = ['forecasts_to_dom']


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

    day_forecast = dom.DayForecast()

    for forecast in forecasts:
        for weather in forecast.weather:
            if day_forecast.icon_id is None:
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

    xml = dom.xml()
    forecast = dom.Forecast()
    forecast.day.append(_day_dom(today_forecasts))
    forecast.day.append(_day_dom(tomorrow_forecasts))
    forecast.day.append(_day_dom(day_after_tomorrow_forecasts))
    xml.forecast = forecast
    xml.name = city
    xml.pubdate = now.strftime('%Y-%m-%d %H:%M:%S')
    return xml
