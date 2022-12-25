from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 25')


def snafu_to_digit(snafu):
    dnumber = 0
    for i in range(len(snafu)):
        pos=len(snafu)-i-1
        if snafu[pos] == '-':
            dnumber -= 5 ** i
        elif snafu[pos] == '=':
            dnumber -= 2 * (5 ** i)
        else:
            dnumber += int(snafu[pos]) * (5 ** i)
    return dnumber


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = ''
    while n:
        digits+=str(int(n % b))
        n //= b
    return digits[::-1]


def base5_to_snafu(s):
    snafu=''
    s=list(s)
    for i in range(len(s)):
        pos=len(s)-1-i
        if s[pos] in '012':
            snafu = s[pos]+snafu
        else:
            if s[pos]=='4':
                snafu = '-'+snafu
            else:
                snafu = '=' + snafu
            k=1
            while pos-k>=0 and int(s[pos-k])+1==5:
                s[pos-k]='0'
                k+=1
            if pos-k<0:
                snafu='1'+snafu
                break
            else:
                s[pos - k]=str(int(s[pos-k])+1)

    return snafu


def f(example):
    s = example.split('\n')

    digit_list=[]
    for snafu in s:
        digit_list.append(snafu_to_digit(snafu))
    dsum=sum(digit_list)

    print('Solution for part 1 is:', base5_to_snafu(numberToBase(dsum, 5)))
    print('Solution for part 2 is complete! We have fifty stars! Marry Christmas!')


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
