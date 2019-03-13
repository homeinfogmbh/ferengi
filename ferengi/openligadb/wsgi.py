"""WSGI interface."""

from wsgilib import XML

from ferengi.openligadb.dom import ArrayOfBlTableTeam
from ferengi.openligadb.orm import Team


__all__ = ['ROUTES']


def get_table():
    """Returns the table of the 1st Bundesliga."""

    table = ArrayOfBlTableTeam()

    for record in Team:
        table.append(record.to_dom())

    return XML(table)


ROUTES = (('GET', '/openligadb/table', get_table, 'get_openligadb_table'),)
