"""Abstract base classes for database tables"""

from peewee import Model, MySQLDatabase, PrimaryKeyField
from .config import ferengi_config

__all__ = ['FerengiModel']


class FerengiModel(Model):
    """Generic FERENGI database Model"""

    class Meta:
        database = MySQLDatabase(
            ferengi_config.db['db'],
            host=ferengi_config.db['host'],
            user=ferengi_config.db['user'],
            passwd=ferengi_config.db['passwd'])
        schema = database.database

    id = PrimaryKeyField()
