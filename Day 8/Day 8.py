from definitions import read_inputs
import numpy as np
import math

input_example, puzzle_input = read_inputs('Day 8')

def monotonic1(x):
    if x.shape[1]==1:
        m = x.transpose().copy()
    else:
        m=x.copy()
    if m.shape[1]==2:
        return True
    if m[0,-1]>m[0,1:-1].max():
        return True
    return False

def monotonic2(x):
    if x.shape[1]==1:
        m = x.transpose().copy()
    else:
        m=x.copy()
    if m.shape[1]==2:
        return True
    if m[0, 0]>m[0,1:-1].max():
        return True
    return False


def calorie_counting(example):
    s = example.split('\n')
    s=[[int(i) for i in k] for k in s]
    n=len(s)
    ns = np.matrix(s)
    visible = [0] * n
    for i in range(n):
        visible[i] = [0] * n
    d={}
    for i in range(n):
        for j in range(n):
            d[i,j]=[0,0,0,0]
        left = -1
        right = -1
        up=-1
        down=-1
        for j in range(n):
            if s[i][j]>left:
                left=s[i][j]
                visible[i][j]=1
            if s[i][-1-j]>right:
                right=s[i][-1-j]
                visible[i][-1-j]=1
            if s[j][i]>up:
                up=s[j][i]
                visible[j][i]=1
            if s[-1-j][i]>down:
                down=s[-1-j][i]
                visible[-1-j][i]=1

            for k in range(j):
                #raste pa desno
                if monotonic1(ns[i,k:j+1]) :
                    d[i,j] = [sum(x) for x in zip(d[i,j], [0,1,0,0])]
                #opada pa levo
                if monotonic2(ns[i,k:j+1]):
                    d[i, k] = [sum(x) for x in zip(d[i,k], [1,0,0,0])]

            for k in range(i):
                if monotonic1(ns[k:i + 1, j]):
                    d[i, j] = [sum(x) for x in zip(d[i, j], [0, 0, 0, 1])]

                if monotonic2(ns[k:i + 1, j]):
                    d[k, j] = [sum(x) for x in zip(d[k, j], [0, 0, 1, 0])]
    maxp=0
    for key in d:
        if math.prod(d[key])>maxp:
            maxp=math.prod(d[key])
    print('Solution for part 1 is:', sum(sum(visible,[])))
    print('Solution for part 2 is:', maxp)


print('\ninput_example')
calorie_counting(input_example)
print('\npuzzle_input')
calorie_counting(puzzle_input)
