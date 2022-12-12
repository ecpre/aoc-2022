import sys
import math

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

topography = open(sys.argv[1], 'r')

topomap = []
#really ugly and i hate it
orddict = {'S': 97, 'E': 122}
for i in range(97,123):
    orddict.update({chr(i):i})
nodes = []

class Node:
    def __init__(self,nodesymb,neighbors):
        self.nodesymb = nodesymb
        self.neighbors = neighbors

while True:
    line = topography.readline()
    linecontent = line.strip()

    if not line:
        break
    
    topomap.append(list(linecontent))

topography.close()

def findneighbors(symb,i,j):
    neighbors = []
    if i < len(topomap)-1 and orddict[topomap[i+1][j]]-symb < 2:
        neighbors.append(j + len(topomap[i])*(i+1))
    if i > 0 and orddict[topomap[i-1][j]]-symb < 2:
        neighbors.append(j + len(topomap[i])*(i-1))
    if j < len(topomap[i])-1 and orddict[topomap[i][j+1]]-symb < 2:
        neighbors.append((j + len(topomap[i])*(i))+1)
    if j > 0 and orddict[topomap[i][j-1]]-symb < 2:
        neighbors.append((j + len(topomap[i])*(i))-1)
    return neighbors
        
startnode = Node('S',[])
endnode = Node('E',[])

for i in range(len(topomap)):
    for j in range(len(topomap[i])):
        symb = topomap[i][j]
        effectivesymb = orddict[symb]
        newnode = Node(symb,findneighbors(effectivesymb,i,j))
        if symb == 'S':
            startnode = newnode
        elif symb == 'E':
            endnode = newnode
        nodes.append(newnode)
               

pathlens = []
def search_highest(node):
    bfsqueue = [node]
    visited = [node]
    found = False
    pathlen = 0
    parents = {node: 0}
    
    while not found:
        if len(bfsqueue) == 0:
            return False
        current = bfsqueue.pop(0)
        if current == endnode:
            found = True
            break
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                neighbor = nodes[neighbor]
                bfsqueue.append(neighbor)
                parents.update({neighbor: current})

    pathlen = 1
    current = endnode
    while parents[current] != node:
        current = parents[current]
        pathlen += 1

    pathlens.append(pathlen)

for node in nodes:
    if node.nodesymb == 'a':
        search_highest(node)
        

print(min(pathlens))

    
