from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 2')


def f(example):
    s = example.split('\n')
    shape_p = {'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    victory_p = {'X': 0, 'Y': 3, 'Z': 6}
    score2 = 0
    for game in s:
        # part1
        score += shape_p[game[-1]]
        if ord(game[0]) - ord(game[-1]) == -23:
            score += 3
        elif ord(game[0]) - ord(game[-1]) == -21 or ord(game[0]) - ord(game[-1]) == -24:
            score += 6
        # part2
        score2 += victory_p[game[-1]]
        if game in ['A Y', 'B X', 'C Z']:
            score2 += 1
        elif game in ['A Z', 'B Y', 'C X']:
            score2 += 2
        else:
            score2 += 3
    print('Solution for part 1 is:', score)
    print('Solution for part 2 is:', score2)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
