"""
Manage weather data
"""
__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '11.09.2014'

from hashlib import md5
from datetime import datetime, timedelta
from ..abc import UAC
import requests

class Weather(UAC):
    """
    Receive and store weather data
    """
    # Static data
    __CITIES = {'Hannover': 'DE0004160',
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
    __WEATHER = {'sonnig': 22,
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
    # Configuration
    LIMIT = 1000    # Max. queries per month
    LAST_UPDATE = None   # Start date for counting
    QUERIES = None  # Already performed queries
    BASE_URL = 'http://rwds2.wetter.com/forecast/weather'
    USER_NAME = 'homeinfo'
    API_KEY = 'nBVR6ZsE'
    # Dynamic variables
    __last_update = None
    
    @property
    def up2date(self):
        """
        Determine whether weather is up to date
        """
        if self.__last_update:
            now = datetime.now()
            if now - self.__last_update <= timedelta(days=1):
                return True
            else:
                return False
        else:
            return True
        
    @property
    def quota(self):
        """
        Check if quotas are okay
        """
        if self.QUERIES:
            try:
                queries = int(self.QUERIES)
            except:
                queries = self.LIMIT + 1
            if queries < self.LIMIT:
                return True
        return False
    
    def update(self):
        """
        Conditionally update the weather
        """
        if not self.up2date:
            if self.quota:
                self.__update()
                
    def __update(self):
        """
        Perform update
        """
        for city in self.__CITIES:
            city_code = self.__CITIES[city]
            city_data = self.__get(city_code)
            self.__store(city, city_data)
    
    def __checksum(self, city_code):
        """
        Returns the checksum
        """
        m = md5()
        m.update(''.join([self.USER_NAME, self.API_KEY, city_code]).encode())
        return m.hexdigest()
    
    def __url(self, city_code):
        """
        Returns the search URL
        """
        return '/'.join([self.BASE_URL, 
                         'city', city_code,
                         'user', self.USER_NAME,
                         'cs', self.__checksum(city_code)])
        
    def __get(self, city_code):
        """
        Get weather for the respective city code
        """
        return requests.get(self.__url(city_code))
    
    def __store(self, city, city_data):
        """
        Store weather data to file
        """