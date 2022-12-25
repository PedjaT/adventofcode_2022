import os

days = 0
for c in next(os.walk(os.path.dirname(os.path.abspath(__file__))))[1]:
    if c[:3] == 'Day':
        days += 1

if __name__ == '__main__':
    for d in range(1, days + 1):
        print('Day ' + str(d) + ':')
        s = 'Day ' + str(d) + '.Day ' + str(d)
        globals()[s] = __import__(s)
        print('\n\n')
