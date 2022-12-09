import os


def read_inputs(day):
    cwd = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cwd, day, "input_example")) as file:
        input_example = file.read()
    with open(os.path.join(cwd, day, "puzzle_input")) as file:
        puzzle_input = file.read()
    return input_example, puzzle_input
