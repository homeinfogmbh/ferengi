"""ORM models for the garbage disposal module."""

from __future__ import annotations
from datetime import date

from peewee import CharField
from peewee import IntegerField
from peewee import Model

from ferengi.openligadb import dom
from ferengi.openligadb.client import get_table
from ferengi.openligadb.config import DATABASE, LOGGER


__all__ = ['create_tables', 'Team']


def create_tables():
    """Creates the respective tables."""

    Team.create_table()


class _OpenLigaDBModel(Model):
    """Base Model."""

    class Meta:     # pylint: disable=C0111,R0903
        database = DATABASE
        schema = DATABASE.database


class Team(_OpenLigaDBModel):   # pylint: disable=R0902
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
    def update_from_dom(cls, dom: dom.ArrayOfBlTableTeamType) -> bool:
        """Updates the entire table from the given ArrayOfBlTableTeam."""
        for record in cls:
            LOGGER.info('Removing: %s', record.short_name)
            record.delete_instance()

        for team in dom.BlTableTeam:
            record = cls.from_dom(team)
            record.save()
            LOGGER.info('Added: %s', record.short_name)

        return True

    @classmethod
    def update_from_api(cls) -> bool:
        """Runs an update from the API."""
        year = date.today().year
        LOGGER.info('Getting Bundesliga table for %i.', year)
        dom = get_table(year=year)

        if not dom.BlTableTeam:
            LOGGER.warning('No data for %i.', year)
            year -= 1
            LOGGER.info('Getting Bundesliga table for %i.', year)
            dom = get_table(year=year)

        return cls.update_from_dom(dom)

    @classmethod
    def from_dom(cls, dom: dom.BlTableTeamType) -> Team:
        """Returns a record from a BlTableTeamType instance."""
        record = cls()
        record.draw = dom.Draw
        record.goals = dom.Goals
        record.lost = dom.Lost
        record.matches = dom.Matches
        record.opponent_goals = dom.OpponentGoals
        record.points = dom.Points
        record.short_name = dom.ShortName
        record.team_icon_url = dom.TeamIconUrl
        record.team_info_id = dom.TeamInfoId
        record.team_name = dom.TeamName
        record.won = dom.Won
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
