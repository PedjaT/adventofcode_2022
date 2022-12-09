from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 3')


def priority(ch):
    if ch.isupper():
        prio = ord(ch) - 38
    else:
        prio = ord(ch) - 96
    return prio


def f(example):
    s = example.split('\n')
    prio_sum1 = 0
    prio_sum2 = 0
    counter = 0
    group = []
    for rucksack in s:
        # part1
        ruck_l = len(rucksack)
        comp1 = rucksack[:ruck_l // 2]
        comp2 = rucksack[ruck_l // 2:]
        c = next(iter(set(comp1).intersection(comp2)))
        prio_sum1 += priority(c)
        # part2
        if counter % 3 == 0:
            group = []
        group.append(rucksack)
        if counter % 3 == 2:
            badge = next(iter((set(group[0]).intersection(group[1])).intersection(group[2])))
            prio_sum2 += priority(badge)
        counter += 1

    print('Solution for part 1 is:', prio_sum1)
    print('Solution for part 2 is:', prio_sum2)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
