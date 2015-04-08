"""Manage weather data"""

__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '11.09.2014'

from hashlib import md5
from datetime import datetime, timedelta
import requests
from ..config import weather


class Weather():
    """Receive and store weather data"""

    # Static data
    CITIES = {'Hannover': 'DE0004160',
              'Stuttgart': 'DE0010287',
              'Bielefeld': 'DE0001129',
              'Braunschweig': 'DE0001456',
              'Hameln': 'DE0004132',
              'Braunschweig': 'DE0001456',
              'Hamburg': 'DE0004130',
              'Crailsheim': 'DE0001811',
              'Gaildorf': 'DE0003215',
              'Schwaebisch_Hall': 'DE0009632',
              'Buxtehude': 'DE0001740',
              'Duisburg': 'DE0002289',
              'Passau': 'DE0008145',
              'Herne': 'DE0004490',
              'Ludwigshafen': 'DE0006443'}

    WEATHER = {'sonnig': 22,
               'leicht bewölkt': 13,
               'bedeckt': 12,
               'wolkig': 5,
               'Nebel': 8,
               'Nebel mit Reifbildung': 5,
               'Sprühregen': 15,
               'leichter Sprühregen': 17,
               'starker Sprühregen': 15,
               'leichter Sprühregen, gefrierend': 17,
               'starker Sprühregen, gefrierend': 15,
               'Regen': 15,
               'leichter Regen': 2,
               'mäßiger Regen': 17,
               'starker Regen': 15,
               'leichter Regen, gefrierend': 2,
               'mäßiger od. starker Regen, gefrierend': 17,
               'leichter Schnee-Regen': 16,
               'starker Schnee-Regen': 16,
               'Schnee': 20,
               'leichter Schneefall': 20,
               'mäßiger Schneefall': 20,
               'starker Schneefall': 20,
               'Schauer': 2,
               'leichter Schauer': 2,
               'leichter Regen - Schauer': 2,
               'Regen - Schauer': 2,
               'starker Regen - Schauer': 4,
               'leichter Schnee / Regen - Schauer': 18,
               'starker Schnee / Regen - Schauer': 18,
               'leichter Schnee - Schauer': 3,
               'mäßiger od. starker Schnee - Schauer': 20,
               'Gewitter': 1,
               'leichtes Gewitter': 1,
               'starkes Gewitter': 1,
               'k.A.': 0}

    @property
    def up2date(self):
        """Determines whether weather is up to date"""
        if self._last_update:
            now = datetime.now()
            if now - self._last_update <= timedelta(days=1):
                return True
            else:
                return False
        else:
            return True

    @property
    def quota(self):
        """Checks if quotas are okay"""
        if self.QUERIES:
            try:
                queries = int(self.QUERIES)
            except:
                queries = self.LIMIT + 1
            if queries < self.LIMIT:
                return True
        return False

    @property
    def last_update(self):
        """Returns the last update"""
        pass

    @last_update.setter
    def _last_update(self, last_update):
        """Sets the last update"""
        pass

    @property
    def _queries(self):
        """Returns the used queries"""
        pass

    @_queries.setter
    def _queries(self, queries):
        """Sets the used queries"""
        pass

    @property
    def limit(self):
        """Returns the limit of monthly queries"""
        return int(weather['LIMIT'])

    @property
    def base_url(self):
        """Returns the base URL"""
        return weather['BASE_URL']

    @property
    def user_name(self):
        """Returns the API user name"""
        return weather['USER_NAME']

    @property
    def _api_key(self):
        """Returns the API key"""
        return weather['API_KEY']

    def update(self):
        """Conditionally updates the weather"""
        if not self.up2date:
            if self.quota:
                self._update()

    def _update(self):
        """Perform update"""
        for city in self.CITIES:
            city_code = self.CITIES[city]
            city_data = self._from_api(city_code)
            self._store(city, city_data)

    def _url(self, city_code):
        """Returns the search URL"""
        user = self.user_name
        checksum = md5(''.join([user, self._api_key,
                                city_code]).encode()).hexdigest()
        return '/'.join([self.base_url, 'city', city_code,
                         'user', user, 'cs', checksum])

    def _from_api(self, city_code):
        """Get weather for the respective city code"""
        self._queries += 1
        return requests.get(self._url(city_code))

    def _store(self, city, city_data):
        """Store weather data to file"""
        pass
