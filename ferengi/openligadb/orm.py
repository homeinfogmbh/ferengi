"""ORM models for the OpenLigaDB module."""

from __future__ import annotations
from datetime import date

from peewee import CharField, IntegerField, Model

from peeweeplus import MySQLDatabaseProxy

from ferengi.openligadb.client import get_table
from ferengi.openligadb.config import LOGGER


__all__ = ["create_tables", "Team"]


DATABASE = MySQLDatabaseProxy("ferengi_openligadb", "ferengi.d/openligadb.conf")


def create_tables():
    """Creates the respective tables."""

    Team.create_table()


class _OpenLigaDBModel(Model):
    """Base Model."""

    class Meta:
        database = DATABASE
        schema = DATABASE.database


class Team(_OpenLigaDBModel):
    """Garbage disposal model."""

    draw = IntegerField()
    goals = IntegerField()
    lost = IntegerField()
    matches = IntegerField()
    opponent_goals = IntegerField()
    points = IntegerField()
    short_name = CharField(255)
    team_icon_url = CharField(255)
    team_info_id = IntegerField()
    team_name = CharField(255)
    won = IntegerField()

    @classmethod
    def update_from_table(cls, table: list[dict]) -> bool:
        """Updates the entire table from the given JSON table of team object."""
        for record in cls.select().where(True):
            LOGGER.info("Removing: %s", record.short_name)
            record.delete_instance()

        for team in table:
            record = cls.from_json(team)
            record.save()
            LOGGER.info("Added: %s", record.short_name)

        return True

    @classmethod
    def update_from_api(cls) -> bool:
        """Runs an update from the API."""
        year = date.today().year
        LOGGER.info("Getting Bundesliga table for %i.", year)
        table = get_table(year=year)

        if not table:
            LOGGER.warning("No data for %i.", year)
            year -= 1
            LOGGER.info("Getting Bundesliga table for %i.", year)
            table = get_table(year=year)

        return cls.update_from_table(table)

    @classmethod
    def from_json(cls, team: dict) -> Team:
        """Returns a record from a team JSON object."""
        record = cls()
        record.draw = team.get("draw")
        record.goals = team.get("goals")
        record.lost = team.get("lost")
        record.matches = team.get("matches")
        record.opponent_goals = team.get("opponentGoals")
        record.points = team.get("points")
        record.short_name = team.get("shortName")
        record.team_icon_url = team.get("teamIconUrl")
        record.team_info_id = team.get("teamInfoId")
        record.team_name = team.get("teamName")
        record.won = team.get("won")
        return record
