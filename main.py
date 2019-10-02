import sys
import os
from pathlib import PurePath
from src.Tournament import Tournament


## PROJECT TODOs:
#  - file importing/parsing
#  - Object structures
#    -? SQL backing?
#  - OSX testing
#  - Test suite



arguments = sys.argv
matchday_factory = Matchday_Factory()
matchday_factory.from_cmd(arguments)
