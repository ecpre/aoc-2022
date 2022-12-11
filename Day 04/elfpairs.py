import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

pairs_list = open(sys.argv[1], 'r')

totalscore = 0

elfiterator = 0

while True:
    line = pairs_list.readline()
    linecontent = line.strip()
    
    if not line:
        break
    elf = []

    elfcomma = linecontent.split(',')

    elf1 = elfcomma[0].split('-')
    elf.append(int(elf1[0]))
    elf.append(int(elf1[1]))
    elf1 = elfcomma[1].split('-')
    elf.append(int(elf1[0]))
    elf.append(int(elf1[1]))

    

    if (elf[2] <= elf[0] <= elf[3]) or (elf[0] <= elf[2] <= elf[1]):
        totalscore+=1


        
print(totalscore)
