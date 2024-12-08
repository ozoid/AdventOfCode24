import urllib.request as urllib2
from io import TextIOWrapper

dataurl = 'https://adventofcode.com/2024/day/2/input'

def part1(data):
    totalSafe = 0
    for report in data:
        safe = True
        dir = 0
        report = report.replace('\n','')
        levels = report.split()
        for i in range(1,len(levels)):
            l0 = int(levels[i-1])
            l1 = int(levels[i])
            dist = abs(l1 - l0)
            if dist < 1 or dist > 3:
                safe = False
            if l1 > l0:
                if dir == -1:
                    safe = False
                dir = 1
            if l1 < l0:
                if dir == 1:
                    safe = False
                dir = -1
        if safe:
            totalSafe += 1
    return totalSafe

def testErrors(levels):
    for l in range(0,len(levels)):
        tlevels = levels.copy()
        tlevels.pop(l)
        newreport = ' '.join([str(x) for x in tlevels])
        if part1([newreport]) == 1:
            return True
    return False

def part2(data):
    totalSafe = 0
    for report in data:
        report = report.replace('\n','')
        if part1([report]) == 1:
            totalSafe +=1
            print(f'Safe')
            continue
        levels = report.split()
        if testErrors(levels): 
            print(f'Safe')
            totalSafe +=1
            continue
        print(f'UnSafe')
    return totalSafe

if __name__ == '__main__':
    data = []

    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
        data = TextIOWrapper(response, encoding='utf-8').readlines()

    #while True:
    #    inline = input()
    #    if inline == '':
    #        break
    #    data.append(inline)

    # with open('tmpfile.txt', 'w') as f:
    #     for line in lines:
    #         f.write(f"{line}\n")
    #         data.append(line)
    #exit()
    #with open('tmpfile.txt', 'r') as f:
    #    for line in f.readlines():
    #        data.append(line)

    #print(part1(data))
    print(part2(data))