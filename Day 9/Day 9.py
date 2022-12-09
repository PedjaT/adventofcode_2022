from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 9')


def adjacent(t, h):
    if abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2:
        return True
    return False


def moveknot(t, h):
    if h[0] == t[0] and h[1] > t[1]:
        t[1] += 1
    elif h[0] == t[0] and h[1] < t[1]:
        t[1] -= 1
    elif h[1] == t[1] and h[0] > t[0]:
        t[0] += 1
    elif h[1] == t[1] and h[0] < t[0]:
        t[0] -= 1
    elif h[0] > t[0] and h[1] > t[1]:
        t[1] += 1
        t[0] += 1
    elif h[0] > t[0] and h[1] < t[1]:
        t[1] -= 1
        t[0] += 1
    elif h[0] < t[0] and h[1] > t[1]:
        t[1] += 1
        t[0] -= 1
    else:
        t[1] -= 1
        t[0] -= 1


def f(example):
    s = example.split('\n')

    H = [0, 0]
    visited1 = [[0, 0]]
    visited2 = [[0, 0]]
    d = {}
    for key in range(1, 10):
        d[key] = [0, 0]
    T = [0, 0]
    for move in s:
        for i in range(int(move.split()[1])):
            HP = H.copy()
            if move[0] == 'R':
                H[0] += 1
            if move[0] == 'L':
                H[0] -= 1
            if move[0] == 'U':
                H[1] += 1
            if move[0] == 'D':
                H[1] -= 1
            # part 1
            if not adjacent(T, H):
                T = HP.copy()
                if T not in visited1:
                    visited1.append(T.copy())
            # part 2
            prev = H.copy()
            for knot in d:
                if not adjacent(d[knot], prev):
                    moveknot(d[knot], prev)
                    if knot == 9 and d[knot] not in visited2:
                        visited2.append(d[knot].copy())
                prev = d[knot].copy()

    print('Solution for part 1 is:', len(visited1))
    print('Solution for part 2 is:', len(visited2))


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
