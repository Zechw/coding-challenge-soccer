#!/usr/bin/env python3
import sys
import os
from src.League_Factory import League_Factory


## PROJECT TODOs:
#    -? SQL backing?
#  - OSX testing
#  update Readme; instructions to test/run
#  clean up any stray code?
#  anything else we can test?
#  submit!!


arguments = sys.argv
league_factory = League_Factory()
league_factory.from_cmd(arguments)
league_factory.write_results()
