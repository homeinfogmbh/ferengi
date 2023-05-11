"""OpenWeatherMap API client."""

from __future__ import annotations
from json import loads
from typing import Union

from requests import Response, get

from ferengi.api import APIError
from ferengi.openweathermap.config import CONFIG


__all__ = ['CLIENT']


class Client:
    """Receive and store weather data."""

    def __init__(self, base_url: str, api_key: str, **params):
        """Set base URL and API key"""
        self.base_url = base_url
        self.api_key = api_key
        self.params = params

    def __call__(
            self,
            city_id: int,
            raw: bool = False
    ) -> Union[Response, dict]:
        """Retrieve weather data for the respective city ID."""
        self.params.update({'id': city_id, 'appid': self.api_key})
        response = get(self.base_url, params=self.params)

        if raw:
            return response

        if response.status_code == 200:
            return loads(response.text)

        raise APIError(response)

    @classmethod
    def from_config(cls, **params) -> Client:
        """Return the API config section."""
        return cls(
            CONFIG.get('api', 'base_url'),
            CONFIG.get('api', 'api_key'),
            **params
        )


CLIENT = Client.from_config(units='metric', lang='de')  # Default client.
