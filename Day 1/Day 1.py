from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 1')


def calorie_counting(example):
    s = example.split('\n')
    cal_sums = []
    c = 0
    top_three = 0
    for i in s:
        if i != '':
            c += int(i)
        else:
            cal_sums.append(c)
            c = 0
    cal_sums.append(c)
    print('Solution for part 1 is:', max(cal_sums))
    for i in range(3):
        top_three += max(cal_sums)
        cal_sums.pop(cal_sums.index(max(cal_sums)))
    print('Solution for part 2 is:', top_three)


print('\ninput_example')
calorie_counting(input_example)
print('\npuzzle_input')
calorie_counting(puzzle_input)
