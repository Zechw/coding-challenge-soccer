from src.Team import Team
from src.Game import Game

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
    team.add_game(Game(team, 10, enemy, 0))
    assert team.get_points(1) == 3
    assert team.get_points(2) == 6

def test_get_points_losses():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 0, enemy, 10))
    team.add_game(Game(team, 0, enemy, 10))
    assert team.get_points(1) == 0
    assert team.get_points(2) == 0

def test_get_points_draws():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 10, enemy, 10))
    team.add_game(Game(team, 0, enemy, 0))
    assert team.get_points(1) == 1
    assert team.get_points(2) == 2

def test_get_points_variety():
    team = Team('Santa Cruz Slugs')
    enemy = Team('Aptos FC')
    team.add_game(Game(team, 10, enemy, 0))
    team.add_game(Game(team, 5, enemy, 10))
    team.add_game(Game(team, 5, enemy, 5))
    team.add_game(Game(team, 10, enemy, 10))
    assert team.get_points(4) == 5
