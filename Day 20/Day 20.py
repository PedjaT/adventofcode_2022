from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 20')


def f(example):
    s = example.split('\n')
    n = len(s)
    s = [(i, int(s[i])) for i in range(n)]
    original = s.copy()  # [1, 2, -3, 3, -2, 0, 4]

    s2 = s.copy()
    decryptionkey = 811589153
    s2 = [i + (i[1] * decryptionkey,) for i in s2]

    for id, x in original:
        id1 = s.index((id, x))
        id2 = (id1 + x) % (n - 1)
        tup = s.pop(id1)
        s.insert(id2, tup)
    reslist = []
    for t in s:
        reslist.append(t[1])
    zeroind = reslist.index(0)
    result = 0
    for x in [1000 % (n), 2000 % (n), 3000 % (n)]:
        res = reslist[(zeroind + x) % (n)]
        result += res
    print('Solution for part 1 is:', result)

    original2 = s2.copy()
    for i in range(10):
        for id, x, y in original2:
            id1 = s2.index((id, x, y))
            id2 = (id1 + y) % (n - 1)
            tup = s2.pop(id1)
            s2.insert(id2, tup)

    reslist = []
    for t in s2:
        reslist.append(t[2])
    zeroind = reslist.index(0)
    result = 0
    for x in [1000 % (n), 2000 % (n), 3000 % (n)]:
        res = reslist[(zeroind + x) % (n)]
        result += res

    print('Solution for part 2 is:', result)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
