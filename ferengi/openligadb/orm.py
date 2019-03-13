"""ORM models for the garbage disposal module."""

from peewee import CharField
from peewee import IntegerField
from peewee import Model

from ferengi.openligadb.config import DATABASE, LOGGER
from ferengi.openligadb.dom import BlTableTeam  # pylint: disable=E0611,E0401


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
    def update_from_dom(cls, dom):
        """Updates the entire table from the given ArrayOfBlTableTeam."""
        for record in cls:
            LOGGER.debug('Removing: %i', record)
            record.delete_instance()

        for team in dom.BlTableTeam:
            record = cls.from_dom(team)
            LOGGER.debug('Adding: %i', record)
            record.save()

    @classmethod
    def from_dom(cls, dom):
        """Returns a record from a BlTableTeam DOM instance."""
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

    def to_dom(self):
        """Returns a BlTableTeam DOM instance from the record."""
        dom = BlTableTeam()
        dom.Draw = self.draw
        dom.Goals = self.goals
        dom.Lost = self.lost
        dom.Matches = self.matches
        dom.OpponentGoals = self.opponent_goals
        dom.Points = self.points
        dom.ShortName = self.short_name
        dom.TeamIconUrl = self.team_icon_url
        dom.TeamInfoId = self.team_info_id
        dom.TeamName = self.team_name
        dom.Won = self.won
        return self