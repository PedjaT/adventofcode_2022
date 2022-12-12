from definitions import read_inputs
import sys, copy

input_example, puzzle_input = read_inputs('Day 12')


class Graph():
    def __init__(self, g):
        self.graph = copy.deepcopy(g)
        self.c = len(g[0])
        self.r = len(g)

    def search(self, src, goal):
        dist = []
        visited = []
        for r in range(self.r):
            visited.append([])
            dist.append([])
            visited[r] = [False] * self.c
            dist[r] = [sys.maxsize] * self.c
        visited[src[0]][src[1]] = True
        dist[src[0]][src[1]] = 0
        while not visited[goal[0]][goal[1]]:
            for r in range(self.r):
                for c in range(self.c):
                    if visited[r][c]:
                        continue
                    if c < self.c - 1 and visited[r][c + 1] and self.graph[r][c] - self.graph[r][c + 1] < 2:
                        visited[r][c] = True
                        dist[r][c] = min(dist[r][c + 1] + 1, dist[r][c])
                    if c > 0 and visited[r][c - 1] and self.graph[r][c] - self.graph[r][c - 1] < 2:
                        visited[r][c] = True
                        dist[r][c] = min(dist[r][c - 1] + 1, dist[r][c])
                    if r < self.r - 1 and visited[r + 1][c] and self.graph[r][c] - self.graph[r + 1][c] < 2:
                        visited[r][c] = True
                        dist[r][c] = min(dist[r + 1][c] + 1, dist[r][c])
                    if r > 0 and visited[r - 1][c] and self.graph[r][c] - self.graph[r - 1][c] < 2:
                        visited[r][c] = True
                        dist[r][c] = min(dist[r - 1][c] + 1, dist[r][c])
                    if visited[r][c] and [r, c] == goal:
                        return dist


def f(example):
    s = example.split('\n')
    start = [0, 0]
    end = [0, 0]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'S':
                start = [i, j]
                s[i] = s[i][:j] + 'a' + s[i][j + 1:]
            if s[i][j] == 'E':
                end = [i, j]
                s[i] = s[i][:j] + 'z' + s[i][j + 1:]
    m = [[ord(c) - 97 for c in l] for l in s]

    g = Graph(m)
    step = g.search(start, end)[end[0]][end[1]]
    minstep = step
    for i in range(len(m)):
        # all 'b's are in the first column, and first column if all 'a's, so it is enough to check only for first column
        j = 0
        if m[i][j] == 0:
            newstart = [i, j]
            newstep = g.search(newstart, end)[end[0]][end[1]]
            if newstep < minstep:
                minstep = newstep

    print('Solution for part 1 is:', step)
    print('Solution for part 2 is:', minstep)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
