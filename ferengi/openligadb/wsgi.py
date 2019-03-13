"""WSGI interface."""

from wsgilib import Binary, Error, XML

from ferengi.openligadb.dom import ArrayOfBlTableTeam
from ferengi.openligadb.orm import Team


__all__ = ['ROUTES']


def get_table():
    """Returns the table of the 1st Bundesliga."""

    table = ArrayOfBlTableTeam()

    for record in Team:
        table.append(record.to_dom())

    return XML(table)


def get_icon(ident):
    """Returns the respective team's icon."""

    try:
        team = Team.get(Team.id == ident)
    except Team.DoesNotExist:
        return Error('No such team.', status=404)

    return Binary(team.team_icon)


ROUTES = (
    ('GET', '/openligadb/table', get_table, 'get_openligadb_table'),
    ('GET', '/openligadb/icon/<int:ident>', get_icon,
     'get_openligadb_team_icon'))
