from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 6')


def marker(n, example):
    for i in range(n - 1, len(example)):
        slide = example[i - (n - 1):i + 1]
        if len(set(slide)) == n:
            return i + 1


def f(example):
    print('Solution for part 1 is:', marker(4, example))
    print('Solution for part 2 is:', marker(14, example))


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
