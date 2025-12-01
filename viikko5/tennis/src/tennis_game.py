class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.score_calls = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.match_score1 = 0
        self.match_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.match_score1 = self.match_score1 + 1
        else:
            self.match_score2 = self.match_score2 + 1

    def score_tied(self, score):
        if score < 3:
            return f"{self.score_calls[score]}-All"
        return "Deuce"

    def endgame_score(self, score1, score2):
        difference = score1 - score2
        if difference == 1:
            return f"Advantage {self.player1_name}"
        elif difference == -1:
            return f"Advantage {self.player2_name}"
        elif difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_score(self):
        if self.match_score1 == self.match_score2:
            return self.score_tied(self.match_score1)

        elif self.match_score1 >= 4 or self.match_score2 >= 4:
            return self.endgame_score(self.match_score1, self.match_score2)

        else:
            return f"{self.score_calls[self.match_score1]}-{self.score_calls[self.match_score2]}"
