import urllib.request as urllib2
from io import TextIOWrapper
from itertools import batched
from multiprocessing import Pool

dataurl = 'https://adventofcode.com/2024/day/6/input'

states = ['^','>','v','<']

def nextState(state):
    lstate = len(states)
    state +=1
    if state > lstate -1:
        state = 0
    return state

def part1(data):
    position = [0,0]
    state = 0
    obstacles = []
    distincts = []
    llen = len(data[0].replace('\n',''))
    dlen = len(data) -1
    for y in range(dlen):
        for x in range(llen):
            #print(data[y][x],end='')
            if data[y][x] == '#':
                obstacles.append((y,x))
            if data[y][x] == '^':
                state = 0
                position = [y,x]
                distincts.append((y,x)) # add starting position
                
    while position[0] > -1 and position[0] < dlen and position[1] > -1 and position[1] < llen:
        origpos = position.copy()
        #print(f'{states[state]} Y:{position[0]} X:{position[1]}')
        if state == 0:
            position[0] -= 1
        if state == 1:
            position[1] += 1
        if state == 2:
            position[0] += 1
        if state == 3:
            position[1] -= 1

        hit = sum(1 for h in obstacles if (h[0] == position[0]) and (h[1] == position[1]))
        
        if hit >0:
            state = nextState(state)
            print(f'hit: {position[0]} {position[1]}')
            position[0] = origpos[0]
            position[1] = origpos[1]

        hascovered = sum(1 for p in distincts if (p[0] == position[0]) and (p[1] == position[1]))
        if hascovered == 0:
            distincts.append((position[0],position[1]))
            print(position)
    return len(distincts)-1   # -1 to ignore the step off the page

def dotest(position,obstacles,llen,dlen):
    distincts = []
    state = 0
    obstacleshit = dict()
    while position[0] > -1 and position[0] < dlen and position[1] > -1 and position[1] < llen:
        origpos = position.copy()
        if state == 0:
            position[0] -= 1
        if state == 1:
            position[1] += 1
        if state == 2:
            position[0] += 1
        if state == 3:
            position[1] -= 1
        hit = sum(1 for h in obstacles if (h[0] == position[0]) and (h[1] == position[1]))
        
        if hit >0:
            #id = (position[0] + 1) * (position[1] + 1)
            state = nextState(state)
            #print(f'hit: {id}')
            if (position[0],position[1]) in obstacleshit:
                obstacleshit[(position[0],position[1])] +=1
                if obstacleshit[(position[0],position[1])] > 3:
                    #print(f'loop {(position[0],position[1])}')
                    return []
            else:
                obstacleshit.update({(position[0],position[1]):1})
            position[0] = origpos[0]
            position[1] = origpos[1]
        hascovered = sum(1 for p in distincts if (p[0] == position[0]) and (p[1] == position[1]))
        if hascovered == 0:
            distincts.append((position[0],position[1]))
    
    return distincts

def worker(args):
    place, position, obstacles, llen, dlen = args
    start = position.copy()
    newobs = obstacles.copy()
    if place == start or (place[0] == start[0]-1 and place[1] == start[1]): #on or directly in front of guard
        return 0
    newobs.append(place)
    tmp = dotest(start, newobs, llen, dlen)
    return 1 if len(tmp) == 0 else 0

def testvisited(placesvisited,position,obstacles,llen,dlen):
    count = 0
    total = 0
    for place in placesvisited:
        start = position.copy()
        newobs = obstacles.copy()
        newobs.append(place)
        tmp = dotest(start,newobs,llen,dlen)
        if len(tmp) == 0:
            #print(f'loop {place}')
            total += 1
        count += 1
        print(f'\r{count}',end='')
    return total

def testvisited1(placesvisited, position, obstacles, llen, dlen):
    allplaces = []
    for i in range(dlen):
        for j in range(llen):
            allplaces.append((i,j))
    
    tasks = [(place, position, obstacles, llen, dlen) for place in allplaces]
    total_tasks = len(tasks)
    completed = 0
    # with Pool() as pool:
    #     results = pool.map(worker, tasks)
    with Pool() as pool:
        results_list = []
        for result in pool.imap_unordered(worker, tasks):
            results_list.append(result)
            completed += 1
            print(f"\rCompleted {completed} of {total_tasks} ({(completed/total_tasks)*100:.2f}%)", end='')
    print()  # newline after loop finishes

    return sum(results_list)
    #return sum(results)

def part2(data):
    obstacles = []
    position = []
    llen = len(data[0].replace('\n',''))
    dlen = len(data) 
    for y in range(dlen):
        for x in range(llen):
            if data[y][x] == '#':
                obstacles.append((y,x))
            if data[y][x] == '^':
                position = [y,x]
    start = position.copy()

    placesvisited = dotest(start,obstacles,llen,dlen)
    print(f'Visited:{len(placesvisited)} ')
    total = testvisited1(placesvisited,position,obstacles,llen,dlen)
    return total

if __name__ == '__main__':
    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
       data = TextIOWrapper(response, encoding='utf-8').readlines()
   
   # data =  '....#.....\n'
    # data += '.........#\n'
    # data += '..........\n'
    # data += '..#.......\n'
    # data += '.......#..\n'
    # data += '..........\n'
    # data += '.#..^.....\n'
    # data += '........#.\n'
    # data += '#.........\n'
    # data += '......#...\n'
    #print(part1(data.split('\n')))
    print(part2(data))