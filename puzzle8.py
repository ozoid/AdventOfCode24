import urllib.request as urllib2
from io import TextIOWrapper
import math

dataurl = 'https://adventofcode.com/2024/day/8/input'

def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 3
    return fib(n - 1) + fib(n - 2)

def calcantinodes(pos0,pos1):
    rdiff = pos0[0] - pos1[0]
    cdiff = pos0[1] - pos1[1]
    a0 = pos0[0] + rdiff
    a1 = pos0[1] + cdiff
    b0 = pos1[0] - rdiff
    b1 = pos1[1] - cdiff
    return [(a0,a1),(b0,b1)]

def recurseanti(nodein,steps,dlen,llen,dir):
    newnodes = []
    node = list(nodein)
    while node[0] > -1 and node[0] < dlen and node[1] > -1 and node[1] < llen:
        if dir == 0:
            node[0] += steps[0]
            node[1] += steps[1]
        else:
            node[0] -= steps[0]
            node[1] -= steps[1]
        newnodes.append((node[0],node[1]))
    return newnodes

def parsenodes(data,dlen,llen):
    nodes = {}
    for r in range(dlen):
        for c in range(llen):
            ch = data[r][c]
            if ch != '.':
                if ch in nodes.keys():
                    nodes[data[r][c]].append((r,c))
                else:
                    nodes[data[r][c]] = [(r,c)]
    return nodes

def printoutput(nodes,antinodes,dlen,llen):
    output = ''
    for r in range(dlen):
        for c in range(llen):
            o = '.'
            if (r,c) in antinodes:
                o = '#'
            else:
                for n in nodes:
                    if (r,c) in nodes[n]:
                        o = data[r][c]
                        break
            output += o
        output += '\n'
    print(output)

def part1(data):
    antinodes = []
    llen = len(data[0].replace('\n',''))
    dlen = len(data)
    nodes = parsenodes(data,dlen,llen)
    for n in nodes:
        nlen = len(nodes[n])
        if nlen  < 2:
            continue
        numopts = 1
        if nlen > 2:
            numopts = fib(nlen-1)
        for i in range(numopts):
            for j in range(i,nlen-1):
                ans = calcantinodes(nodes[n][i],nodes[n][j+1])
                if ans[0] not in antinodes:
                    antinodes.append(ans[0])
                if ans[1] not in antinodes:
                    antinodes.append(ans[1])
    antinodes = [x for x in antinodes if x[0] > -1 and x[1] > -1 and x[0] < dlen and x[1] < llen]
    return len(antinodes)
                
def part2(data):
    antinodes = []
    llen = len(data[0].replace('\n',''))
    dlen = len(data)
    nodes = parsenodes(data,dlen,llen)
    for n in nodes:
        nlen = len(nodes[n])
        if nlen  < 2:
            continue
        numopts = 1
        if nlen > 2:
            numopts = fib(nlen-1)
        for i in range(numopts):
            for j in range(i,nlen-1):
                n0 = nodes[n][i]
                n1 = nodes[n][j+1]
                rdiff = n0[0] - n1[0]
                cdiff = n0[1] - n1[1]
                antinodes += recurseanti(n0,(rdiff,cdiff),dlen,llen,0)
                antinodes += recurseanti(n1,(rdiff,cdiff),dlen,llen,0)
                antinodes += recurseanti(n0,(rdiff,cdiff),dlen,llen,1)
                antinodes += recurseanti(n1,(rdiff,cdiff),dlen,llen,1)

    antinodes = [*{*antinodes}] ## remove duplicates
    antinodes = [x for x in antinodes if x[0] > -1 and x[1] > -1 and x[0] < dlen and x[1] < llen] ## remove oob

    printoutput(nodes,antinodes,dlen,llen)

    return len(antinodes)


if __name__ == '__main__':
    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
       data = TextIOWrapper(response, encoding='utf-8').readlines()
    print(part2(data))

#     data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""
#     print(part2(data.split('\n')))