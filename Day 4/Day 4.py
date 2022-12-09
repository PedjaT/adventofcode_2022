from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 4')


def f(example):
    s = example.split('\n')
    contain = 0
    overlap = 0
    for pair in s:
        elfs = pair.split(',')
        elf1 = [int(i) for i in elfs[0].split('-')]
        elf2 = [int(i) for i in elfs[1].split('-')]
        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
            contain += 1
        if not (elf1[1] < elf2[0] or elf1[0] > elf2[1]):
            overlap += 1
    print('Solution for part 1 is:', contain)
    print('Solution for part 2 is:', overlap)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
