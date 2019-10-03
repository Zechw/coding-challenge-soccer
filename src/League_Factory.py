import sys
import os
import re
import tempfile
from pathlib import PurePath
from src.League import League
from src.Game import Game
from src.Team import Team

#this class handles accepting data from arguments/stdin, deliniating matchdays, and generating output.
class League_Factory:
    def __init__(self):
        self.output_name = None #None flag defaults to stdout
        self.league = League()

    def from_cmd(self, arguments):
        #check for filename or stdin
        if sys.stdin.isatty() and self.test_path(arguments[1], 'input'):
            try:
                file_handler = open(os.getcwd() + '/' + arguments[1])
                output_index = 2
            except:
                print('The file could not be read:', sys.exc_info())
        else:
            file_handler = sys.stdin
            output_index = 1
        #check for optional output location
        if len(arguments) > output_index and self.test_path(arguments[output_index], 'output'):
            self.output_name = arguments[output_index]
        self.unpack_input(file_handler)

    #unpacks file into league
    def unpack_input(self, file_handler):
        for line in file_handler:
            re_matches = re.search(r'([a-zA-Z ]+) (\d), ([a-zA-Z ]+) (\d)', line)
            if re_matches is None:
                raise Exception('Could not parse line: ' + line)
            team1 = self.league.get_team_by_name(re_matches.group(1))
            if team1 is None:
                team1 = Team(re_matches.group(1))
            team2 = self.league.get_team_by_name(re_matches.group(3))
            if team2 is None:
                team2 = Team(re_matches.group(3))
            score1 = re_matches.group(2)
            score2 = re_matches.group(4)
            self.league.add_game(Game(team1, score1, team2, score2))


    def write_results(self):
        if self.output_name is not None:
            #write to file
            with open(self.output_name, 'w+') as file:
                self.write_results_to_handler(file)
            print('Output written to:', self.output_name)
        else:
            #write to stdout (tmpfile, then echo)
            with tempfile.TemporaryFile('w+') as tmp:
                self.write_results_to_handler(tmp)
                tmp.seek(0)
                print(tmp.read())

    def write_results_to_handler(self, handler):
        #assume each team played one match per matchday,
        # so any teams # of games played == number of matchdays
        for i in range(1, len(self.league.teams[0].games)+1): #+1 since we're starting at 1, not 0
            if i > 1:
                handler.write(os.linesep) #spacer
            handler.write('Matchday ' + str(i) + os.linesep)
            points = self.league.generate_points(i)
            for point_set in points[:3]:
                suffix = 'pt' if point_set[1] == 1 else 'pts'
                handler.write('{}, {} {}'.format(point_set[0].name, point_set[1], suffix) + os.linesep)


    #throws an exception if path isn't valid, to prevent naive filesystem manipulation
    @staticmethod
    def test_path(path_string, type=''):
        path = PurePath(path_string)
        if type != '':
            type = ' ' + type #pad for formatting
        if path.is_absolute():
            raise Exception('Please provide a relative' + type + ' location. Do not start path with /')
        if '..' in path.parts:
            raise Exception('Please provide a relative' + type + ' location. Do not backtrack directories.')
        return True
