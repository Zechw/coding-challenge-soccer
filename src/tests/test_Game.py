from Game import Game
from Team import Team

team1 = Team('First')
team2 = Team('Second')

def test_get_winner_team1():
    game = Game(team1, 10, team2, 4)
    assert game.get_winner() is team1

def test_get_winner_team2():
    game = Game(team1, 2, team2, 4)
    assert game.get_winner() is team2

def test_get_winner_draw():
    game = Game(team1, 3, team2, 3)
    assert game.get_winner() is None
