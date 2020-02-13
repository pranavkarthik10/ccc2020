inputs = int(input())
coordinatesx = []
coordinatesy = []
for _ in range(inputs):
    x = input()
    a = x[0] + x[1]
    if x[1] == ",":
        a = int(x[0])
    else:
        a = int(a)
    if x[2] != ",":
        a = int(x[0]+x[1]+x[2])
    if len(x) - 1 == 3:
        b = x[2] + x[3]
    elif len(x) - 1 == 2:
        b = x[2]
    elif len(x)-1 == 4: 
        b = x[3] + x[4]
    else:
        b = x[4] + x[5] + x[6]
    b = int(b)
    coordinatesx.append(a)
    coordinatesy.append(b)

minx = 0
for j in range(1,len(coordinatesx)):
    if coordinatesx[minx] > coordinatesx[j]:
        minx = j
    coordinatesx[0], coordinatesx[minx] = coordinatesx[minx], coordinatesx[0]


maxx = len(coordinatesx) - 1
for j in range(len(coordinatesx) - 2):
    if coordinatesx[maxx] < coordinatesx[j]:
        maxx = j
    coordinatesx[len(coordinatesx) - 1], coordinatesx[maxx] = coordinatesx[maxx], coordinatesx[len(coordinatesx) - 1]  

miny = 0
for j in range(1,len(coordinatesy)):
    if coordinatesy[miny] > coordinatesy[j]:
        miny = j
    coordinatesy[0], coordinatesy[miny] = coordinatesy[miny], coordinatesy[0]


maxy = len(coordinatesy) - 1
for j in range(len(coordinatesy) - 2):
    if coordinatesy[maxy] < coordinatesy[j]:
        maxy = j
    coordinatesy[len(coordinatesy) - 1], coordinatesy[maxy] = coordinatesy[maxy], coordinatesy[len(coordinatesy) - 1]  


print(str(coordinatesx[0]-1) + "," + str(coordinatesy[0]-1))
print(str(coordinatesx[len(coordinatesx)-1]+1) + "," + str(coordinatesy[len(coordinatesy)-1]+1))