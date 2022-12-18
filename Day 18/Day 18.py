from definitions import read_inputs
import numpy as np

input_example, puzzle_input = read_inputs('Day 18')


def spreadwater(m):
    spread = False
    for i in range(1, 20):
        for j in range(1, 20):
            for k in range(1, 20):
                if (m[i, j, k + 1] == 2 or m[i, j, k - 1] == 2 or m[i, j + 1, k] == 2 or m[i, j - 1, k] == 2 or
                    m[i + 1, j, k] == 2 or m[i - 1, j, k] == 2) and m[i, j, k] == 0:
                    m[i, j, k] = 2
                    spread = True
    return spread


def f(example):
    s = example.split('\n')
    cubes = [[int(i) for i in l.split(',')] for l in s]
    maxsides = len(cubes) * 6

    m = np.zeros([21, 21, 21], dtype=int)

    for c in cubes:
        m[tuple(c)] = 1

    count = 0
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if m[i, j, k] == 1 and m[i, j, k + 1] == 1:
                    count += 1
                if m[i, j, k] == 1 and m[i, j + 1, k] == 1:
                    count += 1
                if m[i, j, k] == 1 and m[i + 1, j, k] == 1:
                    count += 1
                if ((i == 0 or i == 20) or (j == 0 or j == 20) or (k == 0 or k == 20)) and m[i, j, k] == 0:
                    m[i, j, k] = 2

    spreading = 0
    while spreadwater(m):
        spreading += 1

    count2 = 0
    for i in range(1, 20):
        for j in range(1, 20):
            for k in range(1, 20):
                if m[i, j, k] == 0:
                    if m[i, j, k + 1] == 1:
                        count2 += 1
                    if m[i, j, k - 1] == 1:
                        count2 += 1
                    if m[i, j + 1, k] == 1:
                        count2 += 1
                    if m[i, j - 1, k] == 1:
                        count2 += 1
                    if m[i + 1, j, k] == 1:
                        count2 += 1
                    if m[i - 1, j, k] == 1:
                        count2 += 1
    res1 = maxsides - 2 * count
    res2 = res1 - count2

    print('Solution for part 1 is:', res1)
    print('Solution for part 2 is:', res2)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
