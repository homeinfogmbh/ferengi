"""WSGI interface."""

from requests import get

from wsgilib import Binary, Error, XML

from ferengi.openligadb.config import CONFIG
from ferengi.openligadb.dom import ArrayOfBlTableTeam
from ferengi.openligadb.orm import Team


__all__ = ['ROUTES']


def get_table():
    """Returns the table of the 1st Bundesliga."""

    array_of_bl_table_team = ArrayOfBlTableTeam()

    for record in Team:
        team_icon_url = CONFIG['api']['icon_url'].format(record.id)
        bl_table_team = record.to_dom()
        bl_table_team.TeamIconUrl = team_icon_url
        array_of_bl_table_team.BlTableTeam.append(bl_table_team)

    return XML(array_of_bl_table_team)


def get_icon(ident):
    """Proxy the respecive team icons."""

    try:
        team = Team.get(Team.id == ident)
    except Team.DoesNotExist:
        return Error('No such team.', status=404)

    response = get(team.team_icon_url)
    return Binary(response.content)


ROUTES = (
    ('GET', '/openligadb/table', get_table, 'get_openligadb_table'),
    ('GET', '/openligadb/icon/<int:ident>', get_icon,
     'get_openligadb_team_icon'))
