import urllib.request as urllib2
from io import TextIOWrapper
import math

dataurl = 'https://adventofcode.com/2024/day/7/input'

def base(b,n):
    size = math.ceil(math.log(max(1,n),b))
    return ''.join([str(place) for i in range(size,-1,-1) if (place := n//b**i%b) or i<size] or str(0))

def part1(data):
    total = 0
    for line in data:
        bits = line.split(':')
        answer = int(bits[0])
        tests = [int(x) for x in bits[1].strip().split()]   
        numpos = len(tests) -1
        poss = 2 ** numpos
        for i in range(poss):
            calc = tests[0]
            bins = f'{i:b}'.zfill(numpos)
            for j in range(numpos):
                if bins[j] =='0':
                    calc += tests[j + 1]
                if bins[j] =='1':
                    calc *= tests[j + 1]
            if calc == answer:
                total += calc
                break
    return total

def part2(data):
    total = 0
    for line in data:
        bits = line.split(':')
        answer = int(bits[0])
        tests = [int(x) for x in bits[1].strip().split()]   
        numpos = len(tests) -1
        poss = 3 ** numpos
        for i in range(poss):
            calc = tests[0]
            bins = base(3,i).zfill(numpos)
            for j in range(numpos):
                if bins[j] =='0':
                    calc += tests[j + 1]
                if bins[j] =='1':
                    calc *= tests[j + 1]
                if bins[j] =='2':
                    calc = int(str(calc) + str(tests[j + 1]))
            if calc == answer:
                total += calc
                break
    return total

if __name__ == '__main__':
    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
       data = TextIOWrapper(response, encoding='utf-8').readlines()
    print(part2(data))


#     data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""
#     print(part2(data.split('\n')))