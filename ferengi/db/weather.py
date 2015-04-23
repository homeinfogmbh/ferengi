"""Weather data table"""

from peewee import CharField
from .abc import FerengiModel

__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '23.04.2015'
__all__ = ['Weather']


class Weather(FerengiModel):
    """Table for weather data references to XML documents"""

    location = CharField(16)    # The location name
    xml_file = CharField(128)   # The absolute path to the XML file
