#! /usr/bin/env python3
"""Terminal query interface"""

from wsgilib import RestApp
from ferengi.wsgi import ROUTER

application = RestApp(ROUTER, cors=True)
