"""OpenWeatherMap API client."""

from json import loads
from typing import Any, Optional, Union

from requests import Response, get

from ferengi.api import APIError
from ferengi.openweathermap.config import CONFIG


__all__ = ['CLIENT']


class Client:
    """Receive and store weather data."""

    def __init__(
            self,
            base_url: Optional[str] = None,
            api_key: Optional[str] = None,
            **params
    ):
        """Sets base URL and API key"""
        self.base_url = base_url or self.config['base_url']
        self.api_key = api_key or self.config['api_key']
        self.params = params

    def __call__(
            self,
            city_id: int,
            raw: bool = False
    ) -> Union[Response, dict]:
        """Retrievels weather data for the respective city ID."""
        self.params.update({'id': city_id, 'appid': self.api_key})
        response = get(self.base_url, params=self.params)

        if raw:
            return response

        if response.status_code == 200:
            return loads(response.text)

        raise APIError(response)

    @property
    def config(self) -> dict[str, Any]:
        """Returns the API config section."""
        return CONFIG['api']


CLIENT = Client(units='metric', lang='de')   # Default client.
