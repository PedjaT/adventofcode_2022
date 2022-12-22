from definitions import read_inputs
import numpy as np
import re

input_example, puzzle_input = read_inputs('Day 22')


def move1(position, m, move):
    if position[2] == 1:
        for k in range(move):
            if position[1] + 1 < m.shape[1] and m[position[0], position[1] + 1] == 1:
                position[1] += 1
            elif position[1] + 1 < m.shape[1] and m[position[0], position[1] + 1] == 2:
                break
            else:
                b = False
                for i in range(m.shape[1]):
                    if m[position[0], i] == 1:
                        position[1] = i
                        break
                    if m[position[0], i] == 2:
                        b = True
                        break
                if b:
                    break
    if position[2] == 2:
        for k in range(move):
            if position[0] - 1 >= 0 and m[position[0] - 1, position[1]] == 1:
                position[0] -= 1
            elif position[0] - 1 >= 0 and m[position[0] - 1, position[1]] == 2:
                break
            else:
                b = False
                for i in range(m.shape[0] - 1, -1, -1):
                    if m[i, position[1]] == 1:
                        position[0] = i
                        break
                    if m[i, position[1]] == 2:
                        b = True
                        break
                if b:
                    break
    if position[2] == 3:
        for k in range(move):
            if position[1] - 1 >= 0 and m[position[0], position[1] - 1] == 1:
                position[1] -= 1
            elif position[1] - 1 >= 0 and m[position[0], position[1] - 1] == 2:
                break
            else:
                b = False
                for i in range(m.shape[1] - 1, -1, -1):
                    if m[position[0], i] == 1:
                        position[1] = i
                        break
                    if m[position[0], i] == 2:
                        b = True
                        break
                if b:
                    break
    if position[2] == 4:
        for k in range(move):
            if position[0] + 1 < m.shape[0] and m[position[0] + 1, position[1]] == 1:
                position[0] += 1
            elif position[0] + 1 < m.shape[0] and m[position[0] + 1, position[1]] == 2:
                break
            else:
                b = False
                for i in range(m.shape[0]):
                    if m[i, position[1]] == 1:
                        position[0] = i
                        break
                    if m[i, position[1]] == 2:
                        b = True
                        break
                if b:
                    break


def move2(position, m, move):
    if position[2] == 1:
        for k in range(move):
            if position[1] + 1 < m.shape[1] and m[position[0], position[1] + 1] == 1:
                position[1] += 1
            elif position[1] + 1 < m.shape[1] and m[position[0], position[1] + 1] == 2:
                break
            else:
                if position[0] < 50:
                    for i in range(99, 49, -1):
                        if m[149 - position[0], i] == 1:
                            position[0], position[1] = 149 - position[0], i
                            position[2] = 3
                            move1(position, m, move - k - 1)
                            break
                        if m[149 - position[0], i] == 2:
                            break
                elif position[0] < 100:
                    for i in range(49, -1, -1):
                        if m[i, 50 + position[0]] == 1:
                            position[0], position[1] = i, 50 + position[0]
                            position[2] = 2
                            move1(position, m, move - k - 1)
                            break
                        if m[i, 50 + position[0]] == 2:
                            break
                elif position[0] < 150:
                    for i in range(149, 99, -1):
                        if m[49 - (position[0] - 100), i] == 1:
                            position[0], position[1] = 49 - (position[0] - 100), i
                            position[2] = 3
                            move1(position, m, move - k - 1)
                            break
                        if m[49 - (position[0] - 100), i] == 2:
                            break
                else:
                    for i in range(149, 99, -1):
                        if m[i, position[0] - 100] == 1:
                            position[0], position[1] = i, position[0] - 100
                            position[2] = 2
                            move1(position, m, move - k - 1)
                            break
                        if m[i, position[0] - 100] == 2:
                            break
                break
    elif position[2] == 2:
        for k in range(move):
            if position[0] - 1 >= 0 and m[position[0] - 1, position[1]] == 1:
                position[0] -= 1
            elif position[0] - 1 >= 0 and m[position[0] - 1, position[1]] == 2:
                break
            else:
                if position[1] < 50:
                    for i in range(50, 99, 1):
                        if m[50 + position[1], i] == 1:
                            position[0], position[1] = 50 + position[1], i
                            position[2] = 1
                            move1(position, m, move - k - 1)
                            break
                        if m[50 + position[1], i] == 2:
                            break
                elif position[1] < 100:
                    for i in range(0, 50, 1):
                        if m[position[1] + 100, i] == 1:
                            position[0], position[1] = position[1] + 100, i
                            position[2] = 1
                            move1(position, m, move - k - 1)
                            break
                        if m[position[1] + 100, i] == 2:
                            break
                else:
                    for i in range(199, 149, -1):
                        if m[i, position[1] - 100] == 1:
                            position[0], position[1] = i, position[1] - 100
                            move1(position, m, move - k - 1)
                            break
                        if m[i, position[1] - 100] == 2:
                            break

                break
    elif position[2] == 3:
        for k in range(move):
            if position[1] - 1 >= 0 and m[position[0], position[1] - 1] == 1:
                position[1] -= 1
            elif position[1] - 1 >= 0 and m[position[0], position[1] - 1] == 2:
                break
            else:
                if position[0] < 50:
                    for i in range(50):
                        if m[149 - position[0], i] == 1:
                            position[0], position[1] = 149 - position[0], i
                            position[2] = 1
                            move1(position, m, move - k - 1)
                            break
                        if m[149 - position[0], i] == 2:
                            break
                elif position[0] < 100:
                    for i in range(100, 150, 1):
                        if m[i, position[0] - 50] == 1:
                            position[0], position[1] = i, position[0] - 50
                            position[2] = 4
                            move1(position, m, move - k - 1)
                            break
                        if m[i, position[0] - 50] == 2:
                            break
                elif position[0] < 150:
                    for i in range(50, 100, 1):
                        if m[149 - position[0], i] == 1:
                            position[0], position[1] = 149 - position[0], i
                            position[2] = 1
                            move1(position, m, move - k - 1)
                            break
                        if m[149 - position[0], i] == 2:
                            break
                else:
                    for i in range(50):
                        if m[i, position[0] - 100] == 1:
                            position[0], position[1] = i, position[0] - 100
                            position[2] = 4
                            move1(position, m, move - k - 1)
                            break
                        if m[i, position[0] - 100] == 2:
                            break
                break
    elif position[2] == 4:
        for k in range(move):
            if position[0] + 1 < m.shape[0] and m[position[0] + 1, position[1]] == 1:
                position[0] += 1
            elif position[0] + 1 < m.shape[0] and m[position[0] + 1, position[1]] == 2:
                break
            else:
                if position[1] < 50:
                    for i in range(0, 50, 1):
                        if m[i, 100 + position[1]] == 1:
                            position[0], position[1] = i, 100 + position[1]
                            move1(position, m, move - k - 1)
                            break
                        if m[i, 100 + position[1]] == 2:
                            break
                elif position[1] < 100:

                    for i in range(49, -1, -1):
                        if m[position[1] + 100, i] == 1:
                            position[0], position[1] = position[1] + 100, i
                            position[2] = 3
                            move1(position, m, move - k - 1)
                            break
                        if m[position[1] + 100, i] == 2:
                            break
                else:

                    for i in range(99, 49, -1):
                        if m[position[1] - 50, i] == 1:
                            position[0], position[1] = position[1] - 50, i
                            position[2] = 3
                            move1(position, m, move - k - 1)
                            break
                        if m[position[1] - 50, i] == 2:
                            break
                break


def turning(position, turn):
    if turn == 'R':
        if position[2] == 1:
            position[2] = 4
        else:
            position[2] -= 1
    else:
        if position[2] == 4:
            position[2] = 1
        else:
            position[2] += 1


def f(example):
    s = example.split('\n')
    password = s[-1]
    monkeymap = s[:-2]
    maxlen = 1
    for l in monkeymap:
        if len(l) > maxlen:
            maxlen = len(l)
    for i in range(len(monkeymap)):
        while len(monkeymap[i]) < maxlen:
            monkeymap[i] += ' '
    m = np.zeros([len(monkeymap), maxlen])
    for i in range(len(monkeymap)):
        for j in range(maxlen):
            if monkeymap[i][j] == '.':
                m[i, j] = 1
            if monkeymap[i][j] == '#':
                m[i, j] = 2
    for i in range(maxlen):
        if m[0, i] == 1:
            start = [0, i, 1]
            break
    position = start.copy()
    moves = [int(i) for i in re.findall(r'\d+', password)]
    chars = ''.join([i for i in password if not i.isdigit()])
    turns = [moves[0]]
    for i in range(len(chars)):
        turns.append(chars[i])
        turns.append(moves[i + 1])
    for t in turns:
        if isinstance(t, int):
            move1(position, m, t)
        else:
            turning(position, t)

    position[0] += 1
    position[1] += 1
    orientation = 0
    if position[2] == 1:
        orientation = 0
    elif position[2] == 4:
        orientation = 1
    elif position[2] == 3:
        orientation = 2
    elif position[2] == 2:
        orientation = 3
    print('Solution for part 1 is:', position[0] * 1000 + position[1] * 4 + orientation)
    if m.shape[0] > 20:
        # part 2
        position = start.copy()
        for t in turns:
            if isinstance(t, int):
                move2(position, m, t)
            else:
                turning(position, t)
        position[0] += 1
        position[1] += 1
        orientation = 0
        if position[2] == 1:
            orientation = 0
        elif position[2] == 4:
            orientation = 1
        elif position[2] == 3:
            orientation = 2
        elif position[2] == 2:
            orientation = 3
        print('Solution for part 2 is:', position[0] * 1000 + position[1] * 4 + orientation)  # 18322 too high
    else:
        print('Made solution only for cube in the puzzle input')

print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
