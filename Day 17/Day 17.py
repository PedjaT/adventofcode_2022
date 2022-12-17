from definitions import read_inputs
import numpy as np
import copy

input_example, puzzle_input = read_inputs('Day 17')


def cantfall(r, m):
    for i in r[-3]:
        if m[r[i][1] + 1, r[i][0]]:
            return True
    return False


def cantleft(r, m):
    for i in r[-2]:
        if m[r[i][1], r[i][0] - 1]:
            return True
    return False


def cantright(r, m):
    for i in r[-1]:
        if m[r[i][1], r[i][0] + 1]:
            return True
    return False


def newrock(highest, shapecount):
    rock1 = [[3, highest - 4], [4, highest - 4], [5, highest - 4], [6, highest - 4], [0, 1, 2, 3], [0], [3]]  # -
    rock2 = [[4, highest - 4], [3, highest - 5], [4, highest - 5], [5, highest - 5], [4, highest - 6], [0, 1, 3],
             [0, 1, 4], [0, 3, 4]]  # +
    rock3 = [[3, highest - 4], [4, highest - 4], [5, highest - 4], [5, highest - 5], [5, highest - 6], [0, 1, 2],
             [0, 3, 4], [2, 3, 4]]  # reverse L
    rock4 = [[3, highest - 4], [3, highest - 5], [3, highest - 6], [3, highest - 7], [0], [0, 1, 2, 3],
             [0, 1, 2, 3]]  # |
    rock5 = [[3, highest - 4], [3, highest - 5], [4, highest - 4], [4, highest - 5], [0, 2], [0, 1], [2, 3]]  # square
    rocklist = [rock1, rock2, rock3, rock4, rock5]
    rock = rocklist[shapecount % 5]
    return rock


def fall(rock, m, s, pushid, highest, prevravno):
    r = copy.deepcopy(rock)
    if s[pushid] == '>' and not cantright(r, m):
        for i in range(len(r[:-3])):
            r[i][0] += 1
    if s[pushid] == '<' and not cantleft(r, m):
        for i in range(len(r[:-3])):
            r[i][0] -= 1
    pushid += 1
    if pushid == len(s):
        pushid = 0
    while not cantfall(r, m):
        for i in range(len(r[:-3])):
            r[i][1] += 1
        if s[pushid] == '>' and not cantright(r, m):
            for i in range(len(r[:-3])):
                r[i][0] += 1
        if s[pushid] == '<' and not cantleft(r, m):
            for i in range(len(r[:-3])):
                r[i][0] -= 1
        pushid += 1
        if pushid == len(s):
            pushid = 0
    for i in range(len(r[:-3])):
        m[r[i][1], r[i][0]] = 1
        if r[i][1] < highest:
            highest = r[i][1]
    if all(m[highest, :]) == 1:
        prevravno = highest
    return pushid, highest, prevravno


def f(example, maxcount=2022):
    s = example.split('\n')
    s = s[0]
    highest = -1
    shapecount = 0
    prevravno = -1
    pushid = 0
    m = np.zeros([int(2.62 * maxcount), 9], dtype=int)
    m[:, 0] = 1
    m[:, -1] = 1
    m[-1, :] = 1
    highest_list = [0]
    while shapecount < maxcount:
        rock = newrock(highest, shapecount)
        shapecount += 1
        pushid, highest, prevravno = fall(rock, m, s, pushid, highest, prevravno)
        highest_list.append(abs(highest) - 1)

    if maxcount == 2022:
        print('Solution for part 1 is:', abs(highest) - 1)
        if len(s) < 50:
            print('Part 2: no patern like in puzzle_input')
    return abs(highest) - 1


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)

# after every 1745 after first 521 rocks, the highest point is covered area (like floor)
maxcount = 1000000000000
maxcount1 = 521 + (maxcount - 521) % 1745
maxcount2 = 521

# result of first 521 rock + next 1745 rocks multiplied by number of 1745 until maxcount+
# solution for rest calculated as corresponding difference (solution for maxcount1 - solution for maxcount2)
solution = f(puzzle_input, maxcount2) + (f(puzzle_input, maxcount2 + 1745) - f(puzzle_input, maxcount2)) * (
            (maxcount - 521) // 1745) + f(puzzle_input, maxcount1) - f(puzzle_input, maxcount2)

print('Solution for part 2 is:', solution)
