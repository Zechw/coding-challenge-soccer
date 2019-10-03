import pytest
import tempfile
from src.League_Factory import League_Factory

def test_path_valid():
    result = League_Factory.test_path('folder/file.txt')
    assert result == True

def test_path_absolute():
    with pytest.raises(Exception):
        League_Factory.test_path('/top/directory.txt')

def test_path_backtrack():
    with pytest.raises(Exception):
        League_Factory.test_path('back/../track.txt')

def test_unpack_input_invalid_exception():
    lf = League_Factory()
    with pytest.raises(Exception):
        lf.unpack_input('BADINPUT')

def test_unpack_input_proper_lengths():
    #team, matchday, games
    lf = League_Factory()
    with tempfile.TemporaryFile('w+') as tmp:
        tmp.write(
"""San Jose Earthquakes 3, Santa Cruz Slugs 3
Capitola Seahorses 1, Aptos FC 0
Felton Lumberjacks 2, Monterey United 0
Felton Lumberjacks 1, Aptos FC 2
Santa Cruz Slugs 0, Capitola Seahorses 0
Monterey United 4, San Jose Earthquakes 2
Santa Cruz Slugs 2, Aptos FC 3
San Jose Earthquakes 1, Felton Lumberjacks 4
Monterey United 1, Capitola Seahorses 0
Aptos FC 2, Monterey United 0
Capitola Seahorses 5, San Jose Earthquakes 5
Santa Cruz Slugs 1, Felton Lumberjacks 1""")
        tmp.seek(0)
        lf.unpack_input(tmp)
        assert len(lf.league.teams) == 6
        assert len(lf.league.games) == 12
        for team in lf.league.teams:
            assert len(team.games) == 4
