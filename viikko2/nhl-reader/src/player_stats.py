class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        self._players = reader.get_players()
    
    def top_scorers_by_nationality(self, country):
        players_of_country = filter(
            lambda player:
            player.nationality == country,
            self._players
        )
        sorted_players = sorted(
            players_of_country,
            key=lambda player: (player.goals + player.assists, player.goals),
            reverse=True
        )
        return list(sorted_players)