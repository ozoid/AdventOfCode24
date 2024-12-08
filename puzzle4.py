import urllib.request as urllib2
from io import TextIOWrapper

dataurl = 'https://adventofcode.com/2024/day/4/input'
letters = ['M','A','S']
total = 0
rot = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] # clockwise t,tr,r,br,b,bl,l,tl

def checkline(data,dir,x,y,rows,cols):
    ny = y
    nx = x
    for letter in letters:
        ny += rot[dir][0]
        nx += rot[dir][1]
        if ny < 0 or ny > rows-1:
            return False
        if nx < 0 or nx > cols-1:
            return False
        if data[ny][nx] != letter:
            return False
        
    return True

def checkAbout(data,x,y,rows,cols):
    global total
    for i in range(len(rot)):
        result = checkline(data,i,x,y,rows,cols)
        if result:
            total += 1

def part1(data):
    lstr = str(data[0]).replace('\n','')
    cols = len(lstr)
    rows = len(data)
    posX = 0
    posY = 0
    for posY in range(rows):
        for posX in range(cols):
            if data[posY][posX] == 'X':
                checkAbout(data,posX,posY,rows,cols)
    return total

def checkDiags(data,x,y,rows,cols):
    ny = y
    nx = x
    crosscount = 0 
    if (ny - 1) < 0 or (ny + 1) > rows-1:
        return False
    if (nx - 1) < 0 or (nx + 1) > cols-1:
        return False
    if data[ny - 1][nx + 1] == 'M' and data[ny + 1][nx - 1] == 'S':
        crosscount +=1
    if data[ny + 1][nx + 1] == 'M' and data[ny - 1][nx - 1] == 'S':
        crosscount +=1
    if data[ny - 1][nx + 1] == 'S' and data[ny + 1][nx - 1] == 'M':
        crosscount +=1
    if data[ny + 1][nx + 1] == 'S' and data[ny - 1][nx - 1] == 'M':
        crosscount +=1
    if crosscount >1:
        return True
    return False

def part2(data):
    global total
    total = 0
    lstr = str(data[0]).replace('\n','')
    cols = len(lstr)
    rows = len(data)
    posX = 0
    posY = 0
    for posY in range(rows):
        for posX in range(cols):
            if data[posY][posX] == 'A':
                if checkDiags(data,posX,posY,rows,cols):
                    total += 1
    return total

if __name__ == '__main__':
    #data = ['MMMSXXMASM','MSAMXMSMSA','AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSASXSS','SAXAMASAAA','MAMMMXMMMM','MXMXAXMASX']
    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
        data = TextIOWrapper(response, encoding='utf-8').readlines()
    print(part2(data))