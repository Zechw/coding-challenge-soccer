#!/usr/bin/env python3
import sys
import os
from src.League_Factory import League_Factory

arguments = sys.argv
league_factory = League_Factory()
league_factory.from_cmd(arguments)
league_factory.write_results()
