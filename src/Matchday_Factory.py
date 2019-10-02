import sys
from Matchday import Matchday

#this class handles accepting data from arguments, and parsing that into matchdays.
# ?factor out some "league" container or matchdays, or fine as a factory?
class Matchday_Factory:
    def __init__(self):
        self.output_name = 'output.txt' #default
        self.matchdays = []
        self.teams = []
        self.games = []
    def from_cmd(self, arguments):
        input = arguments[0]
        #check for optional output location
        if len(arguments) > 1 and self.test_path(arguments[1], 'output'):
            self.output_name = arguments[1]
        #check for input file and read, else assume stdin
        if string_input[-4:] == '.txt' and self.test_path(string_input, 'input'):
            try:
                with open(os.getcwd() + '/' + string_input) as file:
                #TODO: does cwd need ../, does it need '/', does it need 'r'
                    string_input = file.read()
            except:
                print('The file could not be read:', sys.exc_info())
        #TODO HERE
        # split file into matchdays?
        # need to first determine how many teams in league;
        # or create matches/teams based on this.
        # -- for line: if teamname in knownteams


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
