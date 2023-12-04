from enum  import Enum

class Ties(Enum):
    TIE0 = "Love-All"
    TIE15 = "Fifteen-All"
    TIE30 = "Thirty-All"
    DEUCE = "Deuce"

class Points(Enum):
    POINT0 = "Love"
    POINT15 = "Fifteen"
    POINT30 = "Thirty"
    POINT40 = "Forty"

POINTS_TO_WIN = 4

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, name):
        if name == self.player1_name:
            self.player1_score += 1
        elif name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError("Invalid player name")

    def get_score(self) -> str:
        return self._tie_score(self.player1_score) if self._score_is_tied() else self._scores_to_string()
    
    def _tie_score(self, score) -> str:
        match score:
            case 0:
                return Ties.TIE0.value
            case 1:
                return Ties.TIE15.value
            case 2:
                return Ties.TIE30.value
            case _:
                return Ties.DEUCE.value
    
    def _score_is_tied(self) -> bool:
        return self.player1_score == self.player2_score
            
    def _scores_to_string(self) -> str:
        if self.player1_score >= POINTS_TO_WIN or self.player2_score >= POINTS_TO_WIN:
            difference = self.player1_score - self.player2_score
            if difference == 1:
                return f"Advantage {self.player1_name}"
            elif difference == -1:
                return f"Advantage {self.player2_name}"
            elif difference > 1:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"

        return f"{self._player_points(self.player1_score)}-{self._player_points(self.player2_score)}"
    
    def _player_points(self, score) -> str:
        match score:
            case 0:
                return Points.POINT0.value
            case 1:
                return Points.POINT15.value
            case 2:
                return Points.POINT30.value
            case 3:
                return Points.POINT40.value
