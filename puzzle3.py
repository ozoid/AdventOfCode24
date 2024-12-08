import urllib.request as urllib2
from io import TextIOWrapper
import re

dataurl = 'https://adventofcode.com/2024/day/3/input'

def part1(data):
    exp = r'mul\(\d+?,\d+?\)'
    muls = re.findall(exp,data)
    total = 0
    for mul in muls:
        raw = mul.replace('mul(','').replace(')','')
        splt = raw.split(',')
        x = int(splt[0])
        y = int(splt[1])
        total += (x * y)
    return total

def part2(data):
    #bit upto first don't()
    data = data.replace('\n','')
    begx = r'^(.*?)(?:don\'t\(\))'
    begs = re.findall(begx,data)
    total = 0
    for beg in begs:
        total += part1(beg)
    #from first do() to last don't()
    exp = r'(?:do\(\))(.*?)(?:don\'t\(\))'
    does = re.findall(exp,data)
    for dos in does:
        total += part1(dos)
    #from last do() to end
    endinx = data.rfind('do()')
    print(f'End index: {endinx}')
    endata = data[endinx:]
    total += part1(endata)

    return total

if __name__ == '__main__':
    data = []

    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
        data = TextIOWrapper(response, encoding='utf-8').read()

    print(part2(data))