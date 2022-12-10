import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

instructions = open(sys.argv[1], 'r')

valtotal = 0
vals = [1]
currentcycle = 0

while True:
   line = instructions.readline()
   linecontent = line.strip()

   if not line:
       break

   instruction = linecontent.split(" ")
   if instruction[0] == "noop":
       currentcycle+=1
       vals.append(vals[currentcycle-1])

   if instruction[0] == "addx":
       currentcycle+=1
       vals.append(vals[currentcycle-1])
       currentcycle+=1
       vals.append(vals[currentcycle-1]+int(instruction[1]))

instructions.close()

lit = []

#i'm pretty sure this code is flawed but it still worked so...
for i in range(len(vals)):
    if (i%40 == vals[i]%40-1) or (i%40 == vals[i]%40) or (i%40 == vals[i]%40+1):
        lit.append("#")
    else:
        lit.append(".")

for i in range(6):
    print(''.join(lit[:40]))
    lit = lit[40:]
    





    
    
