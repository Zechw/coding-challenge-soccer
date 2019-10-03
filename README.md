# Jane Coding Test solution

This is my solution for the Jane Soccer Challenge, running on Python 3.
I've confirmed this works on Mac Bash, Windows Bash, and Windows CMD.

## Setup

Simply clone or download this repo. All code and tests execute from the base `coding-challenge-soccer` directory.
Tests require `pytest`, but normal execution doesn't require any additional libraries.

## Running

`python3 main.py input_filename [output_filename]`

The program can be run, either by piping in data, or providing a file location to read from (must be within the project directory or subfolder) to the `main.py` file.

You can optionally provide a second parameter for an output location (must also be within the project directory or subfolder--subfolder must already exist). Be aware that this will overwrite the defined output location without any warning.
If no output location is provided, the output will be printed to stdout.

### Examples

`python3 main.py sample-input.txt`
`python3 main.py sample-input.txt output-file.txt` (Giving output file name)
`cat sample-input.txt | python3 main.py` (sample stdin on Bash)

## Tests

Tests are contained in the `src/tests` folder, but are run from the base directory, the same as `main.py`
Run tests by executing:
`python3 -m pytest -v`
