from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 7')


class Tree:
    def __init__(self, name, parent='/', val=0, ):
        self.val = val
        self.name = name
        self.nodes = {}
        self.parent = parent

    def add_node(self, name):
        self.nodes[name] = Tree(name, parent=self)

    def __repr__(self):
        return f"Tree({self.name, self.val}): {self.nodes}"


def f(example):
    s = example.split('\n')[1:]
    t = Tree('/')
    current = t
    totalsum = 0
    alldirs = []
    for c in s:
        if c == '$ cd ..':
            x = current.val
            if x <= 100000:
                totalsum += x
            alldirs.append(current.val)
            current = current.parent
            if current == '/':
                current = t
            current.val += x
        elif c == '$ ls':
            continue
        elif c[:5] == '$ cd ':
            current = current.nodes[c[5:]]
        elif c[:4] == 'dir ':
            current.add_node(c[4:])
        else:
            current.val += int(c.split(' ')[0])
    while current.name != '/':
        x = current.val
        if x <= 100000:
            totalsum += x
        alldirs.append(current.val)
        current = current.parent
        current.val += x

    totalsize = t.val
    if totalsize <= 100000:
        totalsum += totalsize

    free = 70000000 - totalsize
    missing = 30000000 - free
    mindir = totalsize

    for d in alldirs:
        if mindir > d >= missing:
            mindir = d

    print('Solution for part 1 is:', totalsum)
    print('Solution for part 2 is:', mindir)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
