import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

elfdict = {
    }

elffile = open(sys.argv[1], 'r')

currentelf = 0

while True:
    line = elffile.readline()

    if not line:
        break
    
    if line.strip() == "":
        currentelf += 1
    elif currentelf in elfdict.keys():
        elfdict.update({currentelf: elfdict[currentelf] + int(line.strip())})
    else:
        elfdict.update({currentelf: int (line.strip())})

elffile.close()

total_calories = 0

for i in range (3):
    max_calories = max(elfdict, key=elfdict.get)
    total_calories += elfdict[max_calories]
    elfdict.pop(max_calories)


print (total_calories)
        
        
