from definitions import read_inputs
from itertools import groupby
import copy

input_example, puzzle_input = read_inputs('Day 5')


def f(example):
    s = example.split('\n')
    d = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    stacks, moves = [list(group) for k, group in groupby(s, lambda x: x == "") if not k]
    stacks.reverse()
    stacks.pop(0)
    for line in stacks:
        i = 1
        j = 1
        while i < len(line):
            if line[i] != ' ':
                d[j].append(line[i])
            j += 1
            i += 4
    d2 = copy.deepcopy(d)

    for move in moves:
        m = [int(i) for i in move.split(' ')[1::2]]
        for i in range(m[0]):
            d[m[2]].append(d[m[1]].pop())
        d2[m[2]] = d2[m[2]] + d2[m[1]][-m[0]:]
        d2[m[1]] = d2[m[1]][:-m[0]]

    result1 = ''
    result2 = ''
    for i in range(1, 10):
        if d[i]:
            result1 += d[i][-1]
        if d2[i]:
            result2 += d2[i][-1]

    print('Solution for part 1 is:', result1)
    print('Solution for part 2 is:', result2)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
