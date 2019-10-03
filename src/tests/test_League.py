from League import League
from Team import Team
from Game import Game

def test_teams_getting_set():
    league = League()
    team1 = Team('Santa Cruz Slugs')
    team2 = Team('Aptos FC')
    team3 = Team('Monterey United')
    league.add_game(Game(team1, 10, team2, 0))
    league.add_game(Game(team1, 10, team3, 0))
    assert league.teams.count(team1) == 1
    assert league.teams.count(team2) == 1
    assert league.teams.count(team3) == 1

def test_add_game():
    league = League()
    team1 = Team('Santa Cruz Slugs')
    team2 = Team('Aptos FC')
    game = Game(team1, 10, team2, 0)
    league.add_game(game)
    assert game in league.games
    assert game in team1.games
    assert game in team2.games

def test_sort_points_by_point():
    team1 = Team('Santa Cruz Slugs')
    team2 = Team('Aptos FC')
    points = [(team2, 0),
              (team1, 10)]
    League.sort_points(points)
    assert points == [(team1, 10),
                      (team2, 0)]


def test_sort_points_by_name():
        team1 = Team('Santa Cruz Slugs')
        team2 = Team('Aptos FC')
        points = [(team1, 0),
                  (team2, 0)]
        League.sort_points(points)
        assert points == [(team2, 0),
                          (team1, 0)]

def test_generate_points():
    league = League()
    team1 = Team('Santa Cruz Slugs')
    team2 = Team('Aptos FC')
    league.add_game(Game(team1, 10, team2, 0))
    league.add_game(Game(team1, 0, team2, 0))
    league.add_game(Game(team1, 1, team2, 1))
    assert league.generate_points() == [
        (team1, 5),
        (team2, 2)
    ]
