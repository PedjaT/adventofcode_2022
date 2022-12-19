from definitions import read_inputs
import copy

input_example, puzzle_input = read_inputs('Day 19')


def actions(state, blueprint, part):
    allactions = []
    s = eval(state)
    maxore = max(blueprint[1], blueprint[2], blueprint[4])
    buying = [(0, 0, 0, 0)]

    if s['ore'] // blueprint[4] and s['obsidian'] // blueprint[5]:
        buying.append((0, 0, 0, 1))

    if s['ore'] // blueprint[2] and s['clay'] // blueprint[3] and s['obsbot'] < blueprint[5]:
        buying.append((0, 0, 1, 0))

    canclay = min(s['ore'] // blueprint[1], 1)
    if s['clabot'] == blueprint[3]:
        canclay = 0
    canore = min(s['ore'] // blueprint[0], 1)
    if s['orebot'] == maxore:
        canore = 0

    if canclay and (s['obsbot'] < 3 or part == 1):
        buying.append((0, 1, 0, 0))
    if canore and (s['clabot'] == 0 or part == 1):
        buying.append((1, 0, 0, 0))

    if s['ore'] >= max(blueprint[0], blueprint[1], blueprint[2], blueprint[4]) and (0, 0, 0, 0) in buying:
        buying.remove((0, 0, 0, 0))

    if part == 1 and (0, 0, 0, 1) in buying:
        buying = [(0, 0, 0, 1)]
    elif part == 1 and (0, 0, 1, 0) in buying:
        buying = [(0, 0, 1, 0)]

    if len(buying) == 0:
        buying = [(0, 0, 0, 0)]

    for i in range(len(buying)):
        s = eval(state)
        # SPENDING ORES FOR BOTS
        s['ore'] -= buying[i][0] * blueprint[0] + buying[i][1] * blueprint[1] + buying[i][2] * blueprint[2] + buying[i][
            3] * blueprint[4]
        s['clay'] -= buying[i][2] * blueprint[3]
        s['obsidian'] -= buying[i][3] * blueprint[5]

        # BOTS MAKING ORES
        s['ore'] += s['orebot']
        s['clay'] += s['clabot']
        s['obsidian'] += s['obsbot']
        s['geode'] += s['geobot']

        # ADDING NUMBER OF BOTS
        s['orebot'] += buying[i][0]
        s['clabot'] += buying[i][1]
        s['obsbot'] += buying[i][2]
        s['geobot'] += buying[i][3]

        s['time'] += 1

        allactions.append(str(s))

    return allactions


def posibilities(blueprint, minutes, state, part):
    graph = {str(state): []}
    geodemax = state['geode']
    maxgeaorobots = state['geobot']
    beststate = copy.deepcopy(state)
    starttime = state['time']
    for t in range(starttime + 1, starttime + minutes):
        l = []
        for k in graph:
            if eval(k)['time'] == t - 1:
                l.append(k)
        for k in l:
            act = actions(k, blueprint, part)
            for a in act:
                e = eval(a)
                geodemax = max(geodemax, e['geode'])
                maxgeaorobots = max(maxgeaorobots, e['geobot'])
                if geodemax == e['geode']:
                    beststate = e
                if starttime + minutes - e['time'] < geodemax - e['geode']:
                    act.remove(a)
            graph[k] += act
            for a in act:
                graph[a] = []
    return beststate, geodemax


def f(example):
    state = {'time': 1, 'orebot': 1, 'clabot': 0, 'obsbot': 0, 'geobot': 0, 'ore': 1, 'clay': 0, 'obsidian': 0,
             'geode': 0}
    s = example.split('\n')
    blueprints = [[int(s) for s in l.split() if s.isdigit()] for l in s]
    minutes = 24
    qualitysum = 0
    for i in range(len(blueprints)):
        gr, geo = posibilities(blueprints[i], minutes, state, 1)
        quality = geo * (i + 1)
        qualitysum += quality
    print('Solution for part 1 is:', qualitysum)
    qualityprod = 1
    minutes = 32
    for i in range(min(3, len(blueprints))):
        quality = posibilities(blueprints[i], minutes, state, 2)[1]
        qualityprod *= quality
    print('Solution for part 2 is:', qualityprod)


print('\ninput_example')
f(input_example)
print('\npuzzle_input')
f(puzzle_input)
