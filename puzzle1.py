import urllib.request as urllib2

from io import TextIOWrapper

dataurl = 'https://adventofcode.com/2024/day/1/input'

def part1(cola,colb):
    x = len(cola)
    result = 0
    while x > 0:
        amin = min(cola)
        bmin = min(colb)
        idxamin = cola.index(amin)
        idxbmin = colb.index(bmin)
        result += abs(amin - bmin)
        cola.pop(idxamin)
        colb.pop(idxbmin)
        x -= 1
    return result

def part2(cola,colb):
    total = 0
    for x in cola:
        times = colb.count(x)
        total += x * times 
    return total

if __name__ == '__main__':
    cola = []
    colb = []
    outline = []
    data = []
    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    rp = urllib2.urlopen(rq)
    data = rp.readlines()
    for line in data:
        dplt = line.split()
        cola.append(int(dplt[0]))
        colb.append(int(dplt[1]))
    
    print(part1(cola,colb))
    print(part2(cola,colb))
