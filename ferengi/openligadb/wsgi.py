"""WSGI interface."""

from typing import Union

from requests import get

from wsgilib import Binary, Error, XML

from ferengi.openligadb.config import CONFIG
from ferengi.openligadb.orm import Team


__all__ = ["ROUTES"]


def get_table() -> XML:
    """Returns the table of the 1st Bundesliga."""

    return XML(Team.dump_dom(url_template=CONFIG["api"]["icon_url"]))


def get_icon(ident: int) -> Union[Binary, Error]:
    """Proxy the respective team icons."""

    try:
        team = Team.get(Team.id == ident)
    except Team.DoesNotExist:
        return Error("No such team.", status=404)

    response = get(team.team_icon_url)
    return Binary(response.content)


ROUTES = [
    ("GET", "/openligadb/table", get_table),
    ("GET", "/openligadb/icon/<int:ident>", get_icon),
]
