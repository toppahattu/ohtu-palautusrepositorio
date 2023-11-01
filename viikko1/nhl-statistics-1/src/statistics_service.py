from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by_points(player):
    return (player.points, player.goals)

def sort_by_goals(player):
    return (player.goals, player.assists)

def sort_by_assists(player):
    return (player.assists, player.goals)

class StatisticsService:
    def __init__(self, reader):
        self._reader = reader
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player
        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )
        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        if sort_by is SortBy.POINTS:
            sort_key = sort_by_points
        elif sort_by is SortBy.GOALS:
            sort_key = sort_by_goals
        elif sort_by is SortBy.ASSISTS:
            sort_key = sort_by_assists
        else:
            raise Exception("Unknown sort_by parameter")

        sorted_players = sorted(
            self._players,
            key=sort_key,
            reverse=True
        )
        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1
        return result
