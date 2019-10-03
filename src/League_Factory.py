import sys
import os
import re
from src.League import League
from src.Game import Game
from src.Team import Team
from pathlib import PurePath

#this class handles accepting data from arguments/stdin, deliniating matchdays, and generating output.
class League_Factory:
    def __init__(self):
        self.output_name = 'output.txt' #default
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
            matches = re.search(r'([a-zA-Z ]+) (\d), ([a-zA-Z ]+) (\d)', line)
            if matches is None:
                raise Exception('Could not parse line: ' + line)
            team1 = self.league.get_team_by_name(matches.group(1))
            if team1 is None:
                team1 = Team(matches.group(1))
            team2 = self.league.get_team_by_name(matches.group(3))
            if team2 is None:
                team2 = Team(matches.group(3))
            score1 = matches.group(2)
            score2 = matches.group(4)
            self.league.add_game(Game(team1, score1, team2, score2))


    def write_results(self):
        with open(self.output_name, 'w+') as file:
            for i in range(1, len(self.league.teams[0].games)+1): #+1 to correct 0 offset array
                if i > 1:
                    file.write(os.linesep) #spacer
                file.write('Matchday ' + str(i) + os.linesep)
                points = self.league.generate_points(i)
                for point_set in points[:3]:
                    suffix = 'pt' if point_set[1] == 1 else 'pts'
                    file.write('{}, {} {}'.format(point_set[0].name, point_set[1], suffix) + os.linesep)


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
