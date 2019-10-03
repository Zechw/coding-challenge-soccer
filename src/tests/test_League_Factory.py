import pytest
from League_Factory import League_Factory


#path validation
def test_path_valid():
    result = League_Factory.test_path('folder/file.txt')
    assert result == True

def test_path_absolute():
    with pytest.raises(Exception):
        League_Factory.test_path('/top/directory.txt')

def test_path_backtrack():
    with pytest.raises(Exception):
        League_Factory.test_path('back/../track.txt')

#League Unpacking
def test_todo():
    pass
    #TODO
