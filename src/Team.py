class Team:
    # change test values if you change these defaults
    POINTS_WIN = 3
    POINTS_DRAW = 1
    PONTS_LOSS = 0

    def __init__(self, name='Unnamed Team'):
        self.name = name
        self.games = []

    def add_game(self, game):
        if game not in self.games:
            self.games.append(game)

    #sums points for the first n games
    def get_points(self, matchdays_to_count):
        points = 0
        for game in self.games[:matchdays_to_count]:
            w = game.get_winner()
            if w is None:
                points += self.POINTS_DRAW
            elif w is self:
                points += self.POINTS_WIN
            else:
                points += self.PONTS_LOSS
        return points
