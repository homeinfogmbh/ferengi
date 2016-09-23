"""Manage weather data"""

from hashlib import md5
from datetime import datetime, timedelta

from requests import get
from peewee import DateTimeField, IntegerField, CharField

from ferengi.config import config
from ferengi.orm import FerengiModel


class WeatherTable(FerengiModel):
    """Weather database table"""

    class Meta:
        db_table = 'weather'

    region = CharField(32)
    last_update = DateTimeField(null=True, default=None)
    queries = IntegerField(default=0)  # This month's queries

    @property
    def up2date(self):
        """Determines whether weather is up to date"""
        if self.last_update is None:
            return False
        else:
            if datetime.now() - self.last_update <= timedelta(days=1):
                return True
            else:
                return False


class WeatherClient():
    """Receive and store weather data"""

    def __call__(self, city_code):
        """Get weather for the respective city code"""
        return get(self.url(city_code))

    @property
    def quota(self):
        """Checks if quotas are okay"""
        # TODO: implement
        pass

    @property
    def config(self):
        """Returns the weather config section"""
        return config['weather']

    @property
    def limit(self):
        """Returns the limit of monthly queries"""
        return int(self.config['LIMIT'])

    @property
    def base_url(self):
        """Returns the base URL"""
        return self.config['BASE_URL']

    @property
    def user_name(self):
        """Returns the API user name"""
        return self.config['USER_NAME']

    @property
    def api_key(self):
        """Returns the API key"""
        return self.config['API_KEY']

    def check_string(self, city_code):
        """Returns the check string for the city code"""
        return ''.join((self.user_name, self.api_key, city_code))

    def checksum(self, city_code):
        """Returns a checksum for the respective city code"""
        return md5(self.check_string(city_code).encode()).hexdigest()

    def url(self, city_code):
        """Returns the search URL"""
        return '/'.join((
            self.base_url, 'city', city_code, 'user', self.user_name,
            'cs', self.checksum(city_code)))

    def update(self):
        """Perform update"""
        for city in self.CITIES:
            self.store(city, self(self.CITIES[city]))


class WeatherTranslator():
    """Translates OpenWeather DOM to Application data"""

    CITIES = {
        'Hannover': 'DE0004160',
        'Stuttgart': 'DE0010287',
        'Bielefeld': 'DE0001129',
        'Braunschweig': 'DE0001456',
        'Hameln': 'DE0004132',
        'Braunschweig': 'DE0001456',
        'Hamburg': 'DE0004130',
        'Crailsheim': 'DE0001811',
        'Gaildorf': 'DE0003215',
        'Schwäbisch Hall': 'DE0009632',
        'Buxtehude': 'DE0001740',
        'Duisburg': 'DE0002289',
        'Passau': 'DE0008145',
        'Herne': 'DE0004490',
        'Ludwigshafen': 'DE0006443'}

    WEATHER = {
        'sonnig': 22,
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

    def __init__(self, dom):
        """Sets the DOM"""
        self.dom = dom

    def __str__(self):
        """Returns the DOM data formatted
        as string for the Flash Application
        """
        return self.application

    @property
    def application(self):
        """Returns the DOM data translated for the Flash Application"""
        pass  # TODO: Implement
