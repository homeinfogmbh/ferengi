"""Common FERENGI API"""

from peeweeplus import MySQLDatabase


__all__['ferengi_database']


def ferengi_database(database, user=None, passwd=None):
    """Returns a local, prefixed database configuration"""

    return MySQLDatabase(
        'ferengi_{}'.format(database),
        host='localhost',
        user=user,
        passwd=passwd)
