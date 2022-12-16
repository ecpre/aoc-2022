import sys
import json

if len(sys.argv) < 2:
    print ("must have an argument")
    exit()

beaconlocs = open(sys.argv[1], 'r')

beacons = set()
sensors = []
taxicabs = []
ineligible_ranges = []

desiredrow = 10

for line in beaconlocs.readlines():
    linecontent = line.strip()

    if not line:
        break
    
    linelist = linecontent.split(" ")

    sensorloc = (int(linelist[2][2:len(linelist[2])-1]), int(linelist[3][2:len(linelist[3])-1]))
    beaconloc = (int(linelist[8][2:len(linelist[8])-1]), int(linelist[9][2:]))

    taxicab = abs(beaconloc[0] - sensorloc[0]) + abs(beaconloc[1]-sensorloc[1])
    beacons.add(beaconloc)
    sensors.append(sensorloc)
    taxicabs.append(taxicab)
    dtc = abs(sensorloc[1] - desiredrow)
    inelrange = [sensorloc[0] - (taxicab-dtc), sensorloc[0] + (taxicab-dtc)]
    if inelrange[1] > inelrange[0]:
        ineligible_ranges.append(inelrange)
    

beaconlocs.close()

totalinel = set()
test = set()

for i in range(4000000):
    ranges = []
    nranges = []
    for j in range(len(sensors)):
        newrange = [sensors[j][0]-(taxicabs[j]-abs(sensors[j][1]-i)), sensors[j][0]+(taxicabs[j]-abs(sensors[j][1]-i))]
        if newrange[1] > newrange[0]:
            ranges.append(newrange)
    ranges.sort()
    nranges.append(ranges[0])
    for interval in ranges[1:]:
        if nranges[-1][0] <= interval[0] <= nranges[-1][-1]:
            nranges[-1][-1] = max(nranges[-1][-1], interval[-1])
        else:
            nranges.append(interval)
    if len(nranges) > 1:
        q = 1
        for j in range(len(nranges)-q):
            if nranges[j+1][0] - nranges[j][1] == 1:
                nranges[j] = [nranges[j][0], nranges[j+1][1]]
                nranges.pop(j+1)
                q+=1
    if len(nranges) > 1:
        print("Beacon found: y=" + str(i) + " x=" + str(nranges[0][1]+1))
        print("Tuning frequency: " + str((nranges[0][1]+1) * 4000000 + i))
        break
        
    
    print(str(i) + " " + str(nranges))
        

for i in range (-3990843, 3990843 + max(taxicabs)):
    if (i, desiredrow) not in beacons:
        for j in range(len(ineligible_ranges)):
            if i >= ineligible_ranges[j][0] and i <= ineligible_ranges[j][1]:
                totalinel.add(i)

print(len(totalinel))
    
print(ineligible_ranges)

