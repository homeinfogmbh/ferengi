"""Abstract base classes for database tables"""

from peewee import Model, MySQLDatabase, PrimaryKeyField
from ..config import db

__author__ = 'Richard Neumann <r.neumann@homeinfo.de>'
__date__ = '23.04.2015'
__all__ = ['FerengiModel']


class FerengiModel(Model):
    """Generic FERENGI database Model"""

    class Meta:
        database = MySQLDatabase(db.get('db'),
                                 host=db.get('host'),
                                 user=db.get('user'),
                                 passwd=db.get('passwd'))
        schema = database.database

    id = PrimaryKeyField()  # The table's primary key
