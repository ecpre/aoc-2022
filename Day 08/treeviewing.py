import sys

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

treemap = open(sys.argv[1], 'r')


trees = []
treedict = {}
rowid = 0

while True:
    line = treemap.readline()
    treerow = line.strip()

    if not line:
        break
    
    trees.append(list(treerow))
    columnid = 0
    for tree in list(treerow):
        treedict.update({str(rowid) + " " + str(columnid): 0})
        columnid += 1
    rowid += 1


# this is really ugly i don't know why i did it this way

for i in range (len(trees)):
    for j in range (len(trees[i])):
        v0 = 0
        k=1
        while True:
            if j+k > len(trees[i])-1:
                break
            if (trees[i][j+k] < trees[i][j]):
                v0 += 1
            else:
                v0 += 1
                break
            k+=1
        v1 = 0
        k=1
        while True:
            if j-k < 0:
                break
            if (trees[i][j-k] < trees[i][j]):
                v1 += 1
            else:
                v1 += 1
                break
            k+=1
        v2 = 0
        k=1
        while True:
            if i+k > len(trees[i])-1:
                break
            if (trees[i+k][j] < trees[i][j]):
                v2 += 1
            else:
                v2 += 1
                break
            k+=1
        v3 = 0
        k=1
        while True:
            if i-k < 0:
                break
            if (trees[i-k][j] < trees[i][j]):
                v3 += 1
            else:
                v3 += 1
                break
            k+=1
        print(str(i) + " " + str(j) + " " + str(v0) + " " + str(v1) + " " + str(v2) + " " + str(v3))
        treedict.update({str(i) + " " + str(j): v0*v1*v2*v3})
            
maxt = 0

for tree in treedict:
    if treedict[tree] > maxt:
        maxt = treedict[tree]


treemap.close()

print(maxt)

