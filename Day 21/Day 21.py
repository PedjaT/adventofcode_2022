from definitions import read_inputs
import copy
from math import floor, ceil

input_example, puzzle_input = read_inputs('Day 21')


def calculate(monkeys, hum):
    if isinstance(hum, int):
        hum = float(hum)
    d = copy.deepcopy(monkeys)
    d['humn'] = hum
    d['root'][1] = '=='
    n1 = d['root'][0]
    n2 = d['root'][2]
    while isinstance(d['root'], list):
        for monkey in d:
            if isinstance(d[monkey], list) and isinstance(d[d[monkey][0]], float) and isinstance(d[d[monkey][2]],
                                                                                                 float):
                d[monkey] = eval(str(d[d[monkey][0]]) + d[monkey][1] + str(d[d[monkey][2]]))
    return d[n1] - d[n2]


def f(example):
    s = example.replace(':', '').split('\n')
    s = [l.split() for l in s]
    d = {}
    for l in s:
        if len(l) == 4:
            d[l[0]] = [l[1], l[2], l[3]]
        else:
            d[l[0]] = float(l[1])
    original = copy.deepcopy(d)
    while isinstance(d['root'], list):
        for monkey in d:
            if isinstance(d[monkey], list) and isinstance(d[d[monkey][0]], float) and isinstance(d[d[monkey][2]],
                                                                                                 float):
                d[monkey] = eval(str(d[d[monkey][0]]) + d[monkey][1] + str(d[d[monkey][2]]))

    x = 1.0
    startdif = calculate(original, x)
    dif = startdif
    while startdif * calculate(original, x) > 0:
        x *= 10
    l = [x / 10, x, calculate(original, x / 10), calculate(original, x)]
    y = l[0] + (l[1] - l[0]) / 2
    counter = 0
    z = calculate(original, y)
    while z != 0 and counter < 60:
        counter += 1
        if z * l[2] < 0:
            l = [l[0], y, l[2], calculate(original, y)]
        else:
            l = [y, l[1], calculate(original, y), l[3]]
        y = l[0] + ceil((l[1] - l[0]) / 2) + 1
        z = calculate(original, y)
        # print(y, z)
    if calculate(original, y) != 0:
        i = l[0]
        while calculate(original, i) != 0 and i <= l[1]:
            i += 1
        y = i

    print('Solution for part 1 is:', d['root'])
    print('Solution for part 2 is:', y)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
