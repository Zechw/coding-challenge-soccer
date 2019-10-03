class Game:
    def __init__(self, team1, score1, team2, score2):
        self.teams = (team1, team2)
        self.score = (score1, score2)

    def get_winner(self):
        if self.score[0] > self.score[1]:
            return self.teams[0]
        if self.score[0] < self.score[1]:
            return self.teams[1]
        return None
