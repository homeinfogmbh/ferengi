"""
Manage weather data
"""
__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '11.09.2014'

from os import system
from hashlib import md5
from datetime import datetime, timedelta
import requests

class Weather():
    """
    Receive and store weather data
    """
    LIMIT = 1000    # Max. queries per month
    LAST_UPDATE = None   # Start date for counting
    QUERIES = None  # Already performed queries
    BASE_URL = 'http://rwds2.wetter.com/forecast/weather'
    USER_NAME = 'homeinfo'
    API_KEY = 'nBVR6ZsE'
    __last_update = None
    
    def __init__(self):
        """
        Constructor
        """
        self.load()
    
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