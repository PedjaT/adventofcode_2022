from definitions import read_inputs
import numpy as np

input_example, puzzle_input = read_inputs('Day 15')


def cantbeacon(s, b, x, row):
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    i = row
    for j in range((s[1] - dist) + abs(s[0] - i), s[1] + dist - abs(s[0] - i) + 1):
        if i == row:
            x[j] = True


def fourlines(s, b):
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1]) + 1
    a1, a2, a3, a4 = (s[0], s[1] - dist), (s[0] - dist, s[1]), (s[0], s[1] + dist), (s[0] + dist, s[1])
    return [(a1, (a2[0] + 1, a2[1] - 1)), (a2, (a3[0] - 1, a3[1] - 1)), (a3, (a4[0] - 1, a4[1] + 1)),
            (a4, (a1[0] + 1, a1[1] + 1))]


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 'ni'  # 'lines do not intersect'
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if x % 1 or y % 1:
        return 'ni'
    return x, y


def inside(p, s, b):
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    if s[0] - dist + s[1] <= p[0] + p[1] <= s[0] + dist + s[1] and s[0] - dist - s[1] <= p[0] - p[1] <= s[0] + dist - s[
        1]:
        return True
    return False


def whichone(pos, s, b):
    for p in pos:
        for i in range(len(s)):
            if inside(p, s[i], b[i]):
                break
            if i == len(s) - 1:
                return p


def f(example):
    s = example.split('\n')
    sandb = [[int(j.split('=')[-1]) for j in
              list(filter(''.__ne__, [i if '=' in i else '' for i in l.replace(',', '').replace(':', '').split()]))]
             for l in s]
    flatten = [item for sublist in sandb for item in sublist]
    maxy, miny, maxx, minx = max(flatten[::2]), min(flatten[::2]), max(flatten[1::2]), min(flatten[1::2])
    x10 = np.zeros(round((maxy - miny) * 1.5), dtype=bool)
    x2000000 = np.zeros(round((maxy - miny) * 1.5), dtype=bool)

    sensors = []
    beacons = []
    for sb in sandb:
        sensors.append([sb[1], sb[0]])
        beacons.append([sb[3], sb[2]])

    for i in range(len(sensors)):
        cantbeacon(sensors[i], beacons[i], x10, 10)
        cantbeacon(sensors[i], beacons[i], x2000000, 2000000)

    for b in beacons:
        if b[0] == 10 and x10[b[1]]:
            x10[b[1]] = False
        if b[0] == 2000000 and x2000000[b[1]]:
            x2000000[b[1]] = False

    if sensors[0] == [18, 2]:
        result = x10.sum()
    else:
        result = x2000000.sum()

    # part 2
    lines = []
    for i in range(len(sensors)):
        flines = fourlines(sensors[i], beacons[i])
        lines += flines
    inters = {}
    for p in lines:
        for q in lines:
            if p != q:
                x, y = line_intersection(p, q)
                if x == 'n':
                    continue
                if (x, y) not in inters:
                    inters[(x, y)] = 1
                else:
                    inters[(x, y)] += 1
    if sensors[0] == [18, 2]:
        possible = []
        for k in inters:
            if 0 <= k[0] <= 20 and 0 <= k[1] <= 20 and inters[k] > 3:
                possible.append(k)
    else:
        possible = []
        for k in inters:
            if 0 <= k[0] <= 4000000 and 0 <= k[1] <= 4000000 and inters[k] > 3:
                possible.append(k)

    point = whichone(possible, sensors, beacons)

    print('Solution for part 1 is:', result)
    print('Solution for part 2 is:', int(point[1] * 4000000 + point[0]))


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
