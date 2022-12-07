import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

commands = open(sys.argv[1], 'r')

directories = {"/": 0}

currentparents = []
current_directory = "/"
summer = 0
sum2 = 0



while True:

    line = commands.readline()
    linecontent = line.strip()

    if not line:
        break

    if linecontent[:4] == "$ cd" and linecontent[5] != '.' and linecontent[5] != '/':
        sum2 += 1
        currentparents.append(current_directory)
        current_directory = linecontent[5:] + str(sum2)
        directories.update({current_directory: 0})
    
        
    if linecontent == "$ cd ..":
        current_directory = currentparents.pop()
        
    if linecontent[0].isnumeric():
        directories.update({current_directory: directories[current_directory] + int(linecontent.split(" ")[0])})
        for parent in currentparents:
            directories.update({parent: directories[parent] + int (linecontent.split(" ")[0])})

commands.close()

totalspace = 70000000
totalspace -= directories["/"]

for directory in directories:
    if directories[directory] < 100001:
        summer += directories[directory]
neededspace = 30000000-totalspace

directoryvals = []

for directory in directories:
   if directories[directory] > neededspace:
       directoryvals.append(directories[directory])


print(summer)
print(totalspace)
print(sum2)
print(min(directoryvals))
            
