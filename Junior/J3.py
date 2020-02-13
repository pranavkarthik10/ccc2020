inputs = int(input())
coordinatesx = []
coordinatesy = []
for _ in range(inputs):
    x = input()
    a = x[0] + x[1]
    if x[1] == ",":
        a = x[0]
    elif x[3] == ",":
        a = x[0]+x[1]+x[2]
    else:
        a = a
    
    if len(x) - 1 == 3:
        if len(a) == 2:
            b = x[3]
        else:
            b = x[2] + x[3]
    elif len(x) - 1 == 2:
        b = x[2]
    elif len(x)-1 == 4: 
        if len(a) == 1:
            b = x[2] + x[3] + x[4]
        elif len(a) == 3:
            b = x[4]
        else:
            b = x[3] + x[4]
    elif len(x)-1 == 5:
        if len(a) == 3:
            b = x[4] + x[5]
        else:
            b = x[4] + x[5] + x[6]

    a = int(a)   
    b = int(b)
    coordinatesx.append(a)
    coordinatesy.append(b)


for i in range(len(coordinatesx)):
    minn = i
    for j in range(i+1,len(coordinatesx)):
        if coordinatesx[minn] > coordinatesx[j]:
            minn = j
    coordinatesx[i], coordinatesx[minn] = coordinatesx[minn], coordinatesx[i]

for i in range(len(coordinatesy)):
    minn = i
    for j in range(i+1,len(coordinatesy)):
        if coordinatesy[minn] > coordinatesy[j]:
            minn = j
    coordinatesy[i], coordinatesy[minn] = coordinatesy[minn], coordinatesy[i]

print(str(coordinatesx[0]-1) + "," + str(coordinatesy[0]-1))
print(str(coordinatesx[len(coordinatesx)-1]+1) + "," + str(coordinatesy[len(coordinatesy)-1]+1))