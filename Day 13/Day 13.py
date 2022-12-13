from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 13')


def rightorder(left, right):
    i = 0
    if len(left) == 0 and len(right):
        return True
    if len(left) and len(right) == 0:
        return False

    if i < len(left) and i < len(right):
        if left[i] == right[i]:
            return rightorder(left[1:], right[1:])
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return True
            else:
                return False
        elif isinstance(left[i], list) and isinstance(right[i], list):
            return rightorder(left[i], right[i])
        elif isinstance(left[i], int):
            return rightorder([left[i]], right[i])
        else:
            return rightorder(left[i], [right[i]])

    return False


def sortedpackets(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x == pivot:
                equal.append(x)
            elif rightorder(x, pivot):
                less.append(x)
            else:
                greater.append(x)
        return sortedpackets(less) + equal + sortedpackets(greater)
    else:
        return array


def f(example):
    s = example.split('\n')
    d = {}
    l = [[[2]], [[6]]]
    for i in range(0, len(s), 3):
        d[i // 3 + 1] = eval(s[i]), eval(s[i + 1])
        l.append(eval(s[i]))
        l.append(eval(s[i + 1]))

    pairsum = 0
    for pair in d:
        if rightorder(d[pair][0], d[pair][1]):
            pairsum += pair
    x = sortedpackets(l)
    print('Solution for part 1 is:', pairsum)
    print('Solution for part 2 is:', (x.index([[2]]) + 1) * (x.index([[6]]) + 1))


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
