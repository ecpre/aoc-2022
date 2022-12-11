import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

data_stream = open(sys.argv[1], 'r')

sofar = ['','','','','','','','','','','','','','']

line = data_stream.readline()
linecontent = line.strip()
    
for i in range(len(linecontent)):
    sofar[i % 14] = linecontent[i]

    if (i>3 and len(set(sofar)) == len(sofar)):
        print(i+1)
        break

data_stream.close()
    
