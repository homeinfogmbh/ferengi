"""ORM models for the OpenLigaDB module."""

from __future__ import annotations
from datetime import date

from peewee import CharField
from peewee import IntegerField
from peewee import Model

from peeweeplus import MySQLDatabaseProxy

from ferengi.openligadb import dom
from ferengi.openligadb.client import get_table
from ferengi.openligadb.config import LOGGER


__all__ = ['create_tables', 'Team']


DATABASE = MySQLDatabaseProxy(
    'ferengi_openligadb',
    'ferengi.d/openligadb.conf'
)


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
    def update_from_dom(
            cls,
            array: dom.ArrayOfBlTableTeamType.typeDefinition
    ) -> bool:
        """Updates the entire table from the given ArrayOfBlTableTeam."""
        for record in cls.select().where(True):
            LOGGER.info('Removing: %s', record.short_name)
            record.delete_instance()

        for team in array.BlTableTeam:
            record = cls.from_dom(team)
            record.save()
            LOGGER.info('Added: %s', record.short_name)

        return True

    @classmethod
    def update_from_api(cls) -> bool:
        """Runs an update from the API."""
        year = date.today().year
        LOGGER.info('Getting Bundesliga table for %i.', year)
        array = get_table(year=year)

        if not array.BlTableTeam:
            LOGGER.warning('No data for %i.', year)
            year -= 1
            LOGGER.info('Getting Bundesliga table for %i.', year)
            array = get_table(year=year)

        return cls.update_from_dom(array)

    @classmethod
    def from_dom(cls, table: dom.BlTableTeamType.typeDefinition) -> Team:
        """Returns a record from a BlTableTeamType instance."""
        record = cls()
        record.draw = table.Draw
        record.goals = table.Goals
        record.lost = table.Lost
        record.matches = table.Matches
        record.opponent_goals = table.OpponentGoals
        record.points = table.Points
        record.short_name = table.ShortName
        record.team_icon_url = table.TeamIconUrl
        record.team_info_id = table.TeamInfoId
        record.team_name = table.TeamName
        record.won = table.Won
        return record

    @classmethod
    def dump_dom(cls, url_template: str = None) -> dom.ArrayOfBlTableTeam:
        """Returns an ArrayOfBlTableTeam."""
        array_of_bl_table_team = dom.ArrayOfBlTableTeam()

        for record in cls:
            bl_table_team = record.to_dom()

            if url_template is not None:
                team_icon_url = url_template.format(record.id)
                bl_table_team.TeamIconUrl = team_icon_url

            array_of_bl_table_team.BlTableTeam.append(bl_table_team)

        return array_of_bl_table_team

    def to_dom(self) -> dom.BlTableTeamType:
        """Returns a BlTableTeamType instance from the record."""
        xml = dom.BlTableTeamType()
        xml.Draw = self.draw
        xml.Goals = self.goals
        xml.Lost = self.lost
        xml.Matches = self.matches
        xml.OpponentGoals = self.opponent_goals
        xml.Points = self.points
        xml.ShortName = self.short_name
        xml.TeamIconUrl = self.team_icon_url
        xml.TeamInfoId = self.team_info_id
        xml.TeamName = self.team_name
        xml.Won = self.won
        return xml
