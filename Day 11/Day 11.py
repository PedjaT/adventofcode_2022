from definitions import read_inputs
import copy

input_example, puzzle_input = read_inputs('Day 11')

rounds = 20
rounds2 = 10000


def f(example):
    s = example.split('\n')
    monkeys = {}
    m = 0
    for l in s:
        if l == '':
            m += 1
            continue
        if m not in monkeys:
            monkeys[m] = [l]
        else:
            monkeys[m].append(l)

    for m in monkeys:
        monkeys[m].pop(0)
        monkeys[m][0] = [int(i) for i in monkeys[m][0].replace(',', '').split()[2:]]
        if '*' in monkeys[m][1]:
            operation = 1
        else:
            operation = 0
        if monkeys[m][1].split()[-1] == 'old':
            monkeys[m][1] = [operation, 'old']
        else:
            monkeys[m][1] = [operation, int(monkeys[m][1].split()[-1])]
        monkeys[m][2] = int(monkeys[m][2].split()[-1])
        monkeys[m][3] = int(monkeys[m][3].split()[-1])
        monkeys[m][4] = int(monkeys[m][4].split()[-1])

    product = 1
    for m in monkeys:
        product *= monkeys[m][2]

    monkeys2 = copy.deepcopy(monkeys)
    inspections = [0] * len(monkeys)
    for round in range(1, rounds + 1):
        for m in monkeys:
            for item in monkeys[m][0]:
                inspections[m] += 1
                if monkeys[m][1][0]:
                    if monkeys[m][1][1] == 'old':
                        item *= item
                    else:
                        item *= monkeys[m][1][1]
                else:
                    if monkeys[m][1][1] == 'old':
                        item += item
                    else:
                        item += monkeys[m][1][1]
                item //= 3
                if item % monkeys[m][2] == 0:
                    monkeys[monkeys[m][3]][0].append(item)
                else:
                    monkeys[monkeys[m][4]][0].append(item)
            monkeys[m][0] = []
    m1 = max(inspections)
    new_list = set(inspections)
    new_list.remove(max(new_list))
    m2 = max(new_list)

    inspections2 = [0] * len(monkeys2)
    for round in range(1, rounds2 + 1):
        for m in monkeys2:
            for item in monkeys2[m][0]:
                inspections2[m] += 1
                if monkeys2[m][1][0]:
                    if monkeys2[m][1][1] == 'old':
                        item *= item
                    else:
                        item *= monkeys2[m][1][1]
                else:
                    if monkeys2[m][1][1] == 'old':
                        item += item
                    else:
                        item += monkeys2[m][1][1]
                item %= product
                if item % monkeys2[m][2] == 0:
                    monkeys2[monkeys2[m][3]][0].append(item)
                else:
                    monkeys2[monkeys2[m][4]][0].append(item)
            monkeys2[m][0] = []
    m21 = max(inspections2)
    new_list = set(inspections2)
    new_list.remove(max(new_list))
    m22 = max(new_list)

    print('Solution for part 1 is:', m1 * m2)
    print('Solution for part 2 is:', m21 * m22)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
