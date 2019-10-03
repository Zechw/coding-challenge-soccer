from Team import Team
from Game import Game

def test_default_name():
    team = Team()
    assert team.name #falsy if None or ''

def test_add_game():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    game = Game(team, 5, enemy, 3)
    team.add_game(game)
    assert game in team.games

def test_get_points_wins():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 10, enemy, 0))
    assert team.get_points() == 3
    team.add_game(Game(team, 10, enemy, 0))
    assert team.get_points() == 6

def test_get_points_losses():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 0, enemy, 10))
    assert team.get_points() == 0
    team.add_game(Game(team, 0, enemy, 10))
    assert team.get_points() == 0

def test_get_points_draws():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 10, enemy, 10))
    assert team.get_points() == 1
    team.add_game(Game(team, 0, enemy, 0))
    assert team.get_points() == 2

def test_get_points_variety():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 10, enemy, 0))
    team.add_game(Game(team, 5, enemy, 10))
    team.add_game(Game(team, 5, enemy, 5))
    team.add_game(Game(team, 10, enemy, 10))
    assert team.get_points() == 5
