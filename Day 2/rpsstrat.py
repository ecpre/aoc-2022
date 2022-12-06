import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

strategy_guide = open(sys.argv[1], 'r')

totalscore = 0

while True:
    line = strategy_guide.readline()
    linecontent = line.strip()

    score = 0

    if not line:
        break

    elif linecontent[0] == 'A' and linecontent[2] == 'X':
        score = 3
    elif linecontent[0] == 'A' and linecontent[2] == 'Y':
        score = 4
    elif linecontent[0] == 'A' and linecontent[2] == 'Z':
        score = 8
    elif linecontent[0] == 'B' and linecontent[2] == 'X':
        score = 1
    elif linecontent[0] == 'B' and linecontent[2] == 'Y':
        score = 5
    elif linecontent[0] == 'B' and linecontent[2] == 'Z':
        score = 9
    elif linecontent[0] == 'C' and linecontent[2] == 'X':
        score = 2
    elif linecontent[0] == 'C' and linecontent[2] == 'Y':
        score = 6
    elif linecontent[0] == 'C' and linecontent[2] == 'Z':
        score = 7
    totalscore += score

strategy_guide.close()

print(totalscore)
    
