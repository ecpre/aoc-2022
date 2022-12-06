import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

stacks = open(sys.argv[1], 'r')

stack1 = ['Q','S','W','C','Z','V','F','T']
stack2 = ['B','R','Q']
stack3 = ['B','Z','T','Q','P','M','S']
stack4 = ['D','V','F','R','Q','H']
stack5 = ['J','G','L','D','B','S','T','P']
stack6 = ['W','R','T','Z']
stack7 = ['H','Q','M','N','S','F','R','J']
stack8 = ['R','N','D','H','W']
stack9 = ['J','Z','T','Q','P','R','B']

stackslist = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]

for i in range(10):      
    line = stacks.readline()

while True:
        
    line = stacks.readline()
    linecontent = line.strip()

    if not line:
        break

    linecontent = linecontent[4:]
    fromsplit = linecontent.split(" from ")
    
    movenum = int(fromsplit[0])

    tofrom = fromsplit[1].split(" to ")

    fromstack = int(tofrom[0])
    to = int(tofrom[1])

    addthis = []
    
    for i in range (movenum):
        if len(stackslist[fromstack-1]) != 0:
            addthis.append(stackslist[fromstack-1].pop())

    addthis.reverse()
    stackslist[to-1].extend(addthis)

print(stackslist)

stacks.close()

    

    
