#! /usr/bin/env python3
"""Bing web API clients"""

from requests import get
from json import loads


class WebService():
    """Basic abstract Bing web service"""
    
    def __init__(self, base_url, api_key):
        """Sets the base URL"""
        self.base_url = base_url
        self.api_key = api_key

    def __call__(self):
        """Calls the API"""
        return get(self.base_url, params=self.params, headers=self.headers)

    @property
    def params(self):
        """Returns the appropriate query parameters"""
        raise NotImplementedError()

    @property
    def headers(self):
        """Returns the appropriate query headers"""
        return {'Ocp-Apim-Subscription-Key': self.api_key}

    @property
    def text(self):
        """Returns the query reply text"""
        return self().text

    @property
    def json(self):
        """Returns the reply as a JSON style dictionary"""
        return loads(self.text)


class NewsSearch(WebService):
    """A news search"""

    def __init__(self, api_key, q, count=None, offset=None, mkt=None,
                 safe_search=None):
        """Sets the search options"""
        super().__init__(
            'https://api.cognitive.microsoft.com/bing/v5.0/news/search',
            api_key)
        self.q = q
        self.count = count
        self.offset = offset
        self.mkt = mkt
        self.safe_search = safe_search

    @property
    def params(self):
        """Returns the parameter dictionary"""
        params = {'q': self.q}

        if self.count is not None:
            params['count'] = self.count

        if self.offset is not None:
            params['offset'] = self.offset

        if self.mkt is not None:
            params['mkt'] = self.mkt

        if self.safe_search is not None:
            params['safeSearch'] = self.safe_search

        return params
