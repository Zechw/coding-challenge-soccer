import sys
import os
from src.League_Factory import League_Factory


## PROJECT TODOs:
#  - file importing/parsing
#  - Object structures
#    -? SQL backing?
#  - OSX testing
#  - Test suite



arguments = sys.argv
league_factory = League_Factory()
league_factory.from_cmd(arguments)
