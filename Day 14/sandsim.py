import sys
import json

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

cavescan = open(sys.argv[1], 'r')

rockandsand = {(0,0)}
#ugly hack that isn't really necessary
rockandsand.remove((0,0))
fallensand = 0
yvalues = {0}

while True:
    line = cavescan.readline()
    linecontent = line.strip()

    if not line:
        break

    linesplit = linecontent.split(" -> ")
    last = linesplit[0].split(",")
    last = (int(last[0]), int(last[1]))
    rockandsand.add(last)
    for i in range (1, len(linesplit)):
        this = linesplit[i].split(",")
        this = (int(this[0]), int(this[1]))
        this2 = this
        rockandsand.add(this)
        while this2[0] < last[0]:
            this2 = (this2[0]+1, this2[1])
            rockandsand.add(this2)
        while this2[0] > last[0]:
            this2 = (this2[0]-1, this2[1])
            rockandsand.add(this2)
        while this2[1] < last[1]:
            this2 = (this2[0], this2[1]+1)
            rockandsand.add(this2)
        while this2[1] > last[1]:
            this2 = (this2[0], this2[1]-1)
            rockandsand.add(this2)
        yvalues.add(this[1])
        last = this

abyss = False
maxy = max(yvalues)+2
#some arbitrarily large value i guess
for i in range (-200, 800):
    rockandsand.add((i, maxy))

#really ugly
while not abyss:
    sandloc = [500,0]
    falling = True
    fallingtime = 0
    while falling:
        if (sandloc[0], sandloc[1]+1) in rockandsand:
            if (sandloc[0]-1, sandloc[1]+1) in rockandsand:
                if (sandloc[0]+1, sandloc[1]+1) in rockandsand:
                    falling = False
                    if sandloc[1] == 0:
                        abyss = True
                        break
                else:
                    sandloc = [sandloc[0]+1, sandloc[1]+1]
            else:
                sandloc = [sandloc[0]-1, sandloc[1]+1]
        else:
            sandloc = [sandloc[0], sandloc[1]+1]
        fallingtime += 1
    rockandsand.add(tuple(sandloc))
    fallensand += 1
           
#print(rockandsand)
print(fallensand)
cavescan.close()
