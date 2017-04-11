#! /usr/bin/env python3
"""Terminal query interface"""

from wsgilib import RestApp
from ferengi.wsgi import SERVICES

application = RestApp(SERVICES, cors=True)
