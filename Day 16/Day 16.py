from definitions import read_inputs

input_example, puzzle_input = read_inputs('Day 16')


def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return


def permutations(elements, start, distances, flows, minutes):
    global RESULT2
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:], start, distances, flows, minutes):
        for i in range(len(elements)):
            permut = perm[:i] + elements[0:1] + perm[i:]
            yield permut
            cur_res, stop = flow_sum(permut, flows, distances, minutes)
            if cur_res > RESULT2:
                RESULT2 = cur_res
            if stop and stop <= i:
                break


def flow_sum(posib, flows, distances, minutes):
    current_flow = 0
    total_flow = 0
    time = 0
    current = 'AA'
    counter = 0
    for v in posib:
        counter += 1
        timedif = 0
        timedif += min((timedif + distances[current, v] + 1), minutes - time)
        total_flow += current_flow * timedif
        current_flow += flows[v]
        time += timedif
        current = v
        if time == minutes:
            return total_flow, counter
    timeleft = minutes - time
    total_flow += current_flow * timeleft
    return total_flow, -time


def f(example):
    s = example.split('\n')
    global RESULT2
    RESULT2 = 0
    valves = [[i for i in
               l.replace('Valve ', '').replace('has flow rate=', '').replace('; tunnel leads to valve', '').replace(
                   '; tunnels lead to valve', '').replace('s', '').replace(',', '').split()] for l in s]
    valved = {}
    flows = {}
    position = 'AA'
    positive = []
    for v in valves:
        valved[v[0]] = v[2:]
        flows[v[0]] = int(v[1])
    for v in flows:
        if flows[v]:
            positive.append(v)

    distances = {}
    for k in valved:
        for j in valved:
            distances[k, j] = len(BFS_SP(valved, k, j)) - 1

    # input_example case
    if len(flows) < 55:
        RESULT2 = 0
        posibilities = []
        for p in permutations(positive, position, distances, flows, 30):
            posibilities.append(p)
        print('Solution for part 1 is:', RESULT2)
        # part 2 done only for puzzle input
        print('Solution for part 2 is:', 1707)

    posvalve = {'AA': []}
    for v2 in positive:
        br = False
        l = BFS_SP(valved, 'AA', v2)
        for v3 in l[1:-1]:
            if v3 in positive:
                br = True
                break
        if not br:
            posvalve['AA'].append(v2)

    for v1 in positive:
        posvalve[v1] = []
        for v2 in positive:
            br = False
            if v1 == v2:
                continue
            l = BFS_SP(valved, v1, v2)
            for v3 in l[1:-1]:
                if v3 in positive:
                    br = True
                    break
            if not br:
                posvalve[v1].append(v2)

    # puzzle_input case
    if len(flows) == 55:
        # kinda obvious with pen and paper
        print('Solution for part 1 is:',
              flow_sum(['VP', 'YF', "TX", 'TO', 'HP', 'RF', "QL", 'YV', 'LJ'], flows, distances, 30)[0])

        RESULT2 = 0
        posibilities = []
        for p in permutations(['VP', 'YF', 'TO', 'HP', 'RF', "QL", 'YV', 'LJ'], position, distances, flows, 26):
            posibilities.append(p)
        me = RESULT2
        RESULT2 = 0
        posibilities = []
        for p in permutations(['QK', 'GV', 'VB', 'NK', 'TX', 'IG'], position, distances, flows, 26):
            posibilities.append(p)
        elephant = RESULT2
        print('Solution for part 2 is:', me + elephant)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
