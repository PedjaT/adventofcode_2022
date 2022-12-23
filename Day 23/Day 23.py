from definitions import read_inputs
import numpy as np

input_example, puzzle_input = read_inputs('Day 23')


def move(point, m, order):
    i, j = point
    for o in order:
        if o == 1:
            if m[i - 1, j - 1] == 0 and m[i - 1, j] == 0 and m[i - 1, j + 1] == 0:
                return i - 1, j
        elif o == 2:
            if m[i + 1, j - 1] == 0 and m[i + 1, j] == 0 and m[i + 1, j + 1] == 0:
                return i + 1, j
        elif o == 3:
            if m[i - 1, j - 1] == 0 and m[i, j - 1] == 0 and m[i + 1, j - 1] == 0:
                return i, j - 1
        else:
            if m[i - 1, j + 1] == 0 and m[i, j + 1] == 0 and m[i + 1, j + 1] == 0:
                return i, j + 1
    return -1, -1


def step(m, order):
    moves = {}
    finished = True
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i, j] and sum(sum(m[i - 1:i + 2, j - 1:j + 2])) > 1:
                finished = False
                x, y = move([i, j], m, order)
                if (x, y) != (-1, -1):
                    if (x, y) not in moves:
                        moves[(x, y)] = [[i, j]]
                    else:
                        moves[(x, y)].append([i, j])
    if finished:
        return 'finished'
    for k in moves:
        if len(moves[k]) == 1:
            m[moves[k][0][0], moves[k][0][1]] = 0
            m[k[0], k[1]] = 1
    order = order[1:] + [order[0]]
    return order


def f(example):
    s = example.split('\n')
    steps = 1000
    m = np.zeros([100 + round(steps / 10), 100 + round(steps / 10)], dtype=int)
    for i in range((m.shape[0] - len(s[0])) // 2, (m.shape[0] - len(s[0])) // 2 + len(s[0])):
        for j in range((m.shape[1] - len(s)) // 2, (m.shape[1] - len(s)) // 2 + len(s)):
            if s[i - (m.shape[0] - len(s[0])) // 2][j - (m.shape[1] - len(s)) // 2] == '#':
                m[i, j] = 1
    order = [1, 2, 3, 4]
    for st in range(steps):
        order = step(m, order)
        if st == 9:
            for i1 in range(m.shape[0]):
                if sum(m[i1, :]):
                    break
            for i2 in range(m.shape[0] - 1, -1, -1):
                if sum(m[i2, :]):
                    break
            for j1 in range(m.shape[1]):
                if sum(m[:, j1]):
                    break
            for j2 in range(m.shape[1] - 1, -1, -1):
                if sum(m[:, j2]):
                    break
            result = ((i2 + 1) - i1) * ((j2 + 1) - j1) - sum(sum(m))
            print('Solution for part 1 is:', result)

        if order == 'finished':
            print('Solution for part 2 is:', st + 1)
            break


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
