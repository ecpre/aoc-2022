import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

rucksack = open(sys.argv[1], 'r')

totalscore = 0

elfiterator = 0



while True:
    line = rucksack.readline()
    linecontent = line.strip()
    
    if not line:
        break

    #string_length = len(linecontent)

    #string1 = linecontent[:len(linecontent)//2]
    #string2 = linecontent[len(linecontent)//2:]
   
    #s1dict = {}
    #s2dict = {}

    #for element in string1:
    #    s1dict.update([(element, True)])
    #for element in string2:
    #    if element in s1dict:
    #        s2dict.update([(element, True)])

    linecontent2 = rucksack.readline().strip()
    linecontnet3 = rucksack.readline().strip()

    s1dict = {}
    s2dict = {}
    s3dict = {}

    for element in linecontent:
        s1dict.update([(element, True)])
    for element in linecontent2:
        if element in s1dict:
            s2dict.update([(element, True)])
    for element in linecontnet3:
        if element in s2dict:
            s3dict.update([(element, True)])
 
    for key in s3dict.keys():
        if key.isupper():
            score = ord(key) - 38
            totalscore += score
        else:
            score = ord(key) - 96
            totalscore += score

 

print(totalscore)
