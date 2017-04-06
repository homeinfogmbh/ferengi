"""Abstract base classes for database tables"""

from peewee import Model, PrimaryKeyField
from peeweeplus import MySQLDatabase

from ferengi.config import config

__all__ = ['FerengiModel']


class FerengiModel(Model):
    """Generic FERENGI database Model"""

    class Meta:
        database = MySQLDatabase(
            config.db['db'],
            host=config.db['host'],
            user=config.db['user'],
            passwd=config.db['passwd'],
            closing=True)
        schema = database.database

    id = PrimaryKeyField()
