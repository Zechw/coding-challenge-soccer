class League:
    def __init__(self):
        self.teams = []
        self.games = [] #TODO do we use this?

    #adds game to Leage and Teams
    def add_game(self, game):
        self.games.append(game)
        for team in game.teams:
            team.add_game(game)
            if team not in self.teams:
                self.teams.append(team)

    #returns list of tuples [(team, points), ...]
    # sorted by points DESC, name ASC
    def generate_points(self):
        points = []
        for team in self.teams:
            points.append( (team, team.get_points()) )
        self.sort_points(points)
        return points

    @staticmethod #in place
    def sort_points(points):
        points.sort(key=lambda x: (x[1] * -1, x[0].name))
