import sys
import json
import functools

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

pairfile = open(sys.argv[1], 'r')

pairs1 = []
pairs2 = []

while True:

    line = pairfile.readline()
    linecontent = line.strip()

    if not line:
        break
    if linecontent != "":
        if linecontent[0] == '[':
            pairs1.append(json.loads(linecontent))
            line = pairfile.readline()
            linecontent = line.strip()
            pairs2.append(json.loads(linecontent))

pairfile.close()

def compare_numbers(pair1, pair2):
    if isinstance(pair1, list) and isinstance(pair2, list):
        lowerlength = min(len(pair1), len(pair2))
        for length in range(lowerlength):
            listret = compare_numbers(pair1[length], pair2[length])
            if listret != None:
                 return listret
        else:
            if len(pair1) > len(pair2):
                return False
            elif len(pair1) < len(pair2):
                return True
            return None
    elif isinstance(pair1, list):
        pair2 = [pair2]
        return compare_numbers(pair1, pair2)
    elif isinstance(pair2, list):
        pair1 = [pair1]
        return compare_numbers(pair1, pair2)
    if pair1 < pair2:
        return True
    if pair1 > pair2:
        return False
    return None


pairtrue = []
#stupid hack instead of changing return of compare_numbers
def compare_numbers_key(pair1,pair2):
    if compare_numbers(pair1,pair2):
        return -1
    elif compare_numbers(pair1,pair2) == False:
        return 1
    return 0

for i in range(len(pairs1)):
    pairtrue.append(compare_numbers(pairs1[i], pairs2[i]))
    
total = 0
for i in range(len(pairtrue)): 
    if pairtrue[i]:
        total+= i+1

totalpairs = pairs1 + pairs2
totalpairs.append([[2]])
totalpairs.append([[6]])
totalpairs.sort(key=functools.cmp_to_key(compare_numbers_key))

print(total)
print((totalpairs.index([[2]])+1) * (totalpairs.index([[6]])+1))
