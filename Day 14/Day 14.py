from definitions import read_inputs
import numpy as np

input_example, puzzle_input = read_inputs('Day 14')

def normalize(c):
    x,y=c.split(',')
    x, y=int(x), int(y)
    x-=450
    return [y,x]

def sanddrop(m, sand):
    if not m[sand[0]+1,sand[1]]:
        sand=[sand[0]+1,sand[1]]
        m[sand[0], sand[1]]=1
        m[sand[0]-1, sand[1]]=0
        return sand
    if not m[sand[0]+1,sand[1]-1]:
        sand=[sand[0]+1,sand[1]-1]
        m[sand[0], sand[1]]=1
        m[sand[0] - 1, sand[1]+1] = 0
        return sand
    if not m[sand[0]+1,sand[1]+1]:
        sand=[sand[0]+1,sand[1]+1]
        m[sand[0], sand[1]]=1
        m[sand[0] - 1, sand[1] - 1] = 0
        return sand
    sand = [0, 50]
    m[sand[0], sand[1]] = 1
    return sand


def f(example):
    s = example.split('\n')
    paths=[[normalize(i) for i in l.split(' -> ')] for l in s]
    flattenlist=[item for sublist in [item for sublist in paths for item in sublist] for item in sublist]
    edge = max(flattenlist[::2]) + 2
    m = np.zeros([max(flattenlist[::2])+3,330], dtype = int)
    counter=0

    for p in paths:
        firstpoint = p[0]
        for i in range(1,len(p)):
            secondpoint=p[i]
            if firstpoint[0]==secondpoint[0]:
                for j in range(min(firstpoint[1], secondpoint[1]),  max(firstpoint[1],secondpoint[1])+1):
                    m[firstpoint[0],j]=1
            if firstpoint[1]==secondpoint[1]:
                for j in range(min(firstpoint[0], secondpoint[0]),  max(firstpoint[0],secondpoint[0])+1):
                    m[j,firstpoint[1]]=1
            firstpoint=p[i]

    x=[0,50]
    while x[0]<edge-1:
        x=sanddrop(m, x)
        if x==[0,50]:
            counter+=1
    m[-1,:]=1
    # print(x)
    count2=counter+1
    while 1:
        y=sanddrop(m,x)
        if x==y and x==[0,50]:
            break
        x=y
        if x==[0,50]:
            count2+=1

    print('Solution for part 1 is:', counter)
    print('Solution for part 2 is:', count2)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
