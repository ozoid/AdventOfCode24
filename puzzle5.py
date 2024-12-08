import urllib.request as urllib2
from io import TextIOWrapper

dataurl = 'https://adventofcode.com/2024/day/5/input'

def part1(rules,updates):
    total = 0
    for update in updates:
        pages = [int(x) for x in update.split(',')]
        valid = True
        for rule in rules:        
            orders = [int(x) for x in rule.split('|')]
            if orders[0] in pages and orders[1] in pages:
                r1 = pages.index(orders[0])
                r2 = pages.index(orders[1])
                if r1 < r2:
                    pass
                else:
                    valid = False
        if valid:          
            middle = int(len(pages)/2)          
            total += pages[middle]
    return total      

def runvalidation(validorders,pages):
    newupdate = pages.copy()
    newvalid = True
    for order in validorders:
        r1 = newupdate.index(order[0])
        r2 = newupdate.index(order[1])
        if r1 > r2:
            newupdate.insert(r2,newupdate.pop(r1))
            newvalid = False
    if newvalid == False:
        newupdate = runvalidation(validorders,newupdate)
    return newupdate


def part2(rules,updates):
    total = 0
    for update in updates:
        validorders = []
        pages = [int(x) for x in update.split(',')]
        valid = True
        for rule in rules:        
            orders = [int(x) for x in rule.split('|')]
            if orders[0] in pages and orders[1] in pages:
                r1 = pages.index(orders[0])
                r2 = pages.index(orders[1])
                validorders.append([orders[0],orders[1]])
                if r1 < r2:
                    pass
                else:
                    valid = False
        if valid == False:
            newupdate = runvalidation(validorders,pages)
            middle = int(len(newupdate)/2)          
            total += newupdate[middle]     
    return total
    
    

if __name__ == '__main__':
    rules = [] #['47|53','97|13','97|61','97|47','75|29','61|13','75|53','29|13','97|29','53|29','61|53','97|53','61|29','47|13','75|47','97|75','47|61','75|61','47|29','75|13','53|13']
    updates = [] # ['75,47,61,53,29','97,61,53,29,13','75,29,13','75,97,47,61,53','61,13,29','97,13,75,29,47']
    rq = urllib2.Request(dataurl)
    rq.add_header('Cookie','session=')
    with urllib2.urlopen(rq) as response:
        data = TextIOWrapper(response, encoding='utf-8').readlines()
    
    for line in data:
        if line.find('|') > 0:
            rules.append(line)
        if line.find(',') > 0:
            updates.append(line)
    print(part2(rules,updates))