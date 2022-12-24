from definitions import read_inputs
import numpy as np

input_example, puzzle_input = read_inputs('Day 24')


def surround(i, j, m):
    sur = []
    if i == 1:
        sur.append((-2, j))
        sur.append((i + 1, j))
    elif i == m.shape[0] - 2:
        sur.append((i - 1, j))
        sur.append((1, j))
    else:
        sur.append((i - 1, j))
        sur.append((i + 1, j))
    if j == 1:
        sur.append((i, -2))
        sur.append((i, j + 1))
    elif j == m.shape[1] - 2:
        sur.append((i, j - 1))
        sur.append((i, 1))
    else:
        sur.append((i, j - 1))
        sur.append((i, j + 1))
    return sur


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            x = greater
            break
        greater += 1
    return x


def nextstate(m1):
    m = m1.copy()
    m2 = np.zeros(m.shape, dtype=int)
    for i in range(1, m.shape[0] - 1):
        for j in range(1, m.shape[1] - 1):
            sur = surround(i, j, m)
            if m[sur[2]] % 10 == 1:
                m2[i, j] += 1
            if (m[sur[1]] - m[sur[1]] % 10) % 100 == 10:
                m2[i, j] += 10
            if (m[sur[3]] - m[sur[3]] % 100) % 1000 == 100:
                m2[i, j] += 100
            if m[sur[0]] // 1000 == 1:
                m2[i, j] += 1000
    for i in range(1, m.shape[0] - 1):
        for j in range(1, m.shape[1] - 1):
            m[i, j] = m2[i, j]
    return m


def allstates(m1):
    number = lcm((m1.shape[0] - 2), (m1.shape[1] - 2))
    m = m1.copy()
    m[0, 1] = 0
    allst = [m]
    for i in range(number - 1):
        allst.append(nextstate(allst[-1]))
    return allst


def nextstates(s, allst, mshape):
    states = []
    all_index, _, current_pos = s
    all_index %= len(allst)
    blizzardstate = allst[all_index]
    x, y = current_pos

    if x + 1 < mshape[0] and blizzardstate[x + 1, y] == 0:
        states.append((all_index, _, (x + 1, y)))
    if y + 1 < mshape[1] and blizzardstate[x, y + 1] == 0:
        states.append((all_index, _, (x, y + 1)))
    if x - 1 >= 0 and blizzardstate[x - 1, y] == 0:
        states.append((all_index, _, (x - 1, y)))
    if y - 1 >= 0 and blizzardstate[x, y - 1] == 0:
        states.append((all_index, _, (x, y - 1)))
    if blizzardstate[x, y] == 0:
        states.append((all_index, _, (x, y)))

    return states


def bfs(m, alstind, cur_pos, goal):
    allst = allstates(m)
    visited = [[alstind, cur_pos]]
    queue = [[alstind, 0, cur_pos]]
    mshape = m.shape
    while queue:
        s = queue.pop(0)
        s[0] += 1
        for i in nextstates(s, allst, mshape):
            allst_index = i[0]
            current_pos = i[2]
            if not (allst_index, current_pos) in visited:
                queue.append([allst_index, s[1] + 1, current_pos])
                visited.append((allst_index, current_pos))
                if current_pos == goal:
                    return s[1] + 1, allst_index


def f(example):
    s = example.split('\n')
    m = np.zeros([len(s), len(s[0])], dtype=int)
    m[0, :] = -9
    m[-1, :] = -9
    m[:, 0] = -9
    m[:, -1] = -9
    m[0, 1] = -1
    m[-1, -2] = 0
    for i in range(1, m.shape[0] - 1):
        for j in range(1, m.shape[1] - 1):
            if s[i][j] == '>':
                m[i, j] = 1
            if s[i][j] == '^':
                m[i, j] = 10
            if s[i][j] == '<':
                m[i, j] = 100
            if s[i][j] == 'v':
                m[i, j] = 1000
    first = bfs(m, 0, (0, 1), (m.shape[0] - 1, m.shape[1] - 2))
    second = bfs(m, first[1], (m.shape[0] - 1, m.shape[1] - 2), (0, 1))
    third = bfs(m, second[1], (0, 1), (m.shape[0] - 1, m.shape[1] - 2))

    print('Solution for part 1 is:', first[0])
    print('Solution for part 2 is:', first[0] + second[0] + third[0])


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
