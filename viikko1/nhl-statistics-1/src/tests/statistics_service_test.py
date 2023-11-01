import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none(self):
        player = self.stats.search("Selänne")
        self.assertEqual(player, None)

    def test_team_returns_players(self):
        players = self.stats.team("EDM")
        names = ["Semenko", "Kurri", "Gretzky"]
        self.assertEqual(len(players), 3)
        for player in players:
            self.assertTrue(player.name in names)

    def test_top_returns_top_three_scorers_without_sort_parameter(self):
        top_scorers = self.stats.top(3)
        top_three = ["Gretzky", "Lemieux", "Yzerman"]
        self.assertEqual(len(top_scorers), 3)
        for player in top_scorers:
            self.assertTrue(player.name in top_three)

    def test_top_returns_top_three_scorers(self):
        top_scorers = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_scorers), 3)
        top_three = ["Gretzky", "Lemieux", "Yzerman"]
        for player in top_scorers:
            self.assertTrue(player.name in top_three)

    def test_top_returns_top_three_goal_scorers(self):
        top_scorers = self.stats.top(3, SortBy.GOALS)
        top_three = ["Lemieux", "Yzerman", "Kurri"]
        self.assertEqual(len(top_scorers), 3)
        for player in top_scorers:
            self.assertTrue(player.name in top_three)

    def test_top_returns_top_three_assist_scorers(self):
        top_scorers = self.stats.top(3, SortBy.ASSISTS)
        top_three = ["Gretzky", "Yzerman", "Lemieux"]
        self.assertEqual(len(top_scorers), 3)
        for player in top_scorers:
            self.assertTrue(player.name in top_three)

    def test_top_raises_exception_with_unknown_sort_parameter(self):
        with self.assertRaises(Exception):
            self.stats.top(3, "kissaistuu")