from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 10')

cycles = [20, 60, 100, 140, 180, 220]


def f(example):
    s = example.split('\n')
    cycle = 1
    X = 1
    result1 = 0
    l = ''
    print('Solution for part 2 is:', )
    for instruction in s:
        sprite = [X - 1, X, X + 1]
        if len(l) in sprite:
            l += '#'
        else:
            l += '.'
        if cycle in cycles:
            result1 += X * cycle
        if cycle % 40 == 0:
            print(l)
            l = ''
        inst = instruction.split()
        if inst[0] == 'noop':
            cycle += 1
            continue
        cycle += 1
        if len(l) in sprite:
            l += '#'
        else:
            l += '.'
        if cycle % 40 == 0:
            print(l)
            l = ''
        if cycle in cycles:
            result1 += X * cycle
        cycle += 1
        X += int(inst[1])

    print('Solution for part 1 is:', result1)
    # print('Solution for part 2 is:', )


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
