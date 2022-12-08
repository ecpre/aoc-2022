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
        treedict.update({str(rowid) + " " + str(columnid): False})
        columnid += 1
    rowid += 1


for i in range (len(trees)):
    minimumheight = -1
    for j in range (len(trees[i])):
        if int(trees[i][j]) > int(minimumheight):
            minimumheight = trees[i][j]
            treedict.update({str(i) + " " + str(j): True})

for i in range (len(trees)):
    minimumheight = -1
    for j in range (len(trees[i])-1, 0, -1):
        if int(trees[i][j]) > int(minimumheight):
            minimumheight = trees[i][j]
            treedict.update({str(i) + " " + str(j): True})

rowwidth = len(trees[0])

for i in range (rowwidth):
    minimumheight = -1
    for j in range (len(trees)):
        if int(trees[j][i]) > int(minimumheight):
            minimumheight = trees[j][i]
            treedict.update({str(j) + " " + str(i): True})
for i in range (rowwidth):
    minimumheight = -1
    for j in range (len(trees)-1, 0, -1):
        if int(trees[j][i]) > int(minimumheight):
            minimumheight = trees[j][i]
            treedict.update({str(j) + " " + str(i): True})
total = 0
for treetrue in treedict:
    if treedict[treetrue] == True:
        total +=1


treemap.close()

print(total)

