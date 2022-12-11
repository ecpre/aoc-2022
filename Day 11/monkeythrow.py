import sys
import math

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

monkeydata = open(sys.argv[1], 'r')

# this probably would have been easier if i used object oriented python... but i don't want to

monkeys = []

monkeyoperations = []

monkeytests = []

monkeytargets = []

monkeyinspections = []

def throw(m1, m2):
    monkeys[m2].append(monkeys[m1].pop(0))

def operation(operations, oldval):
    if operations[0] == "+":
        if operations[1] != "old":
            return oldval + int(operations[1])
        else:
            return oldval + oldval
    elif operations[0] == "*":
        if operations[1] != "old":
            return oldval * int(operations[1])
        else:
            return oldval * oldval

while True:
    line = monkeydata.readline()
    linecontent = line.strip()

    if not line:
        break
    
    linesplit = line.split()
    if linecontent == "":
        pass
    elif linesplit[0] == "Monkey":
        monkeys.append([])
        monkeyinspections.append(0)
    elif linesplit[0] == "Starting":
        monkeys[len(monkeys)-1] = ''.join(linesplit[2:]).split(",")
        print(monkeys[len(monkeys)-1])
    elif linesplit[0] == "Operation:":
        monkeyoperations.append(linesplit[4:])
    elif linesplit[0] == "Test:":
        monkeytests.append(linesplit[3])
    elif linesplit[1] == "true:":
        ttarget = (int(linesplit[5]))
        line = monkeydata.readline()
        linecontent = line.strip()
        linesplit = line.split()
        ftarget = (int(linesplit[5]))
        monkeytargets.append([ttarget, ftarget])

monkeydata.close()

modeverything = 1

#int is unbound so this actually does nothing except make it not take a very, very, very long time.
for num in monkeytests:
    modeverything *= int(num)

for i in range(10000):
    for j in range(len(monkeys)):
        for k in range(len(monkeys[j])):
            newworry = operation(monkeyoperations[j], int(monkeys[j][0]))%modeverything
            monkeys[j][0] = newworry
            monkeyinspections[j] += 1
            if newworry % int(monkeytests[j]) == 0:
                throw(j, monkeytargets[j][0])
            else:
                throw(j, monkeytargets[j][1])

m1 = max(monkeyinspections)
monkeyinspections.pop(monkeyinspections.index(m1))
m2 = max(monkeyinspections)

print(m1*m2)
                
    
    

    

