import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

movements = open(sys.argv[1], 'r')

positions_visited = ["0, 0"]

xpos = [0,0,0,0,0,0,0,0,0,0]
ypos = [0,0,0,0,0,0,0,0,0,0]

lastx = [0,0,0,0,0,0,0,0,0,0]
lasty = [0,0,0,0,0,0,0,0,0,0]

def tailVisit():
    if not (str(xpos[9]) + ", " + str(ypos[9])) in positions_visited:
        positions_visited.append(str(xpos[9]) + ", " +str(ypos[9]))

while True:
    line = movements.readline()
    linecontent = line.strip()

    command = linecontent.split(" ")

    if not line:
        break

    for i in range(int(command[1])):

        if command[0] == "R" or command[0] == "L":
            if command[0] == "R":
                xpos[0] += 1
            else:
                xpos[0] -=1
        else:
            if command[0] == "U":
                ypos[0] += 1
            else:
                ypos[0] -=1
        
        for j in range(9):
            if abs(xpos[j] - xpos[j+1]) > 1:
                if xpos[j] > xpos[j+1]:
                    xpos[j+1] += 1
                else:
                    xpos[j+1] -=1
                if ypos[j] > ypos[j+1]:
                    ypos[j+1] += 1
                elif ypos[j+1] > ypos[j]:
                    ypos[j+1] -=1
            elif abs(ypos[j] - ypos[j+1]) > 1:
                if ypos[j] > ypos[j+1]:
                    ypos[j+1] += 1
                else:
                    ypos[j+1] -=1
                if xpos[j] > xpos[j+1]:
                    xpos[j+1] += 1
                elif xpos[j+1] > xpos[j]:
                    xpos[j+1] -=1
            if j == 8:
                tailVisit()
                

movements.close()

print(len(positions_visited))
                

    


