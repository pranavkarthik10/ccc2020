import math

r = int(input())
c = int(input())

room = []

for _ in range(r):
    i = input().split()
    room.append(i)

def escape(rr, cc):

    if r == rr and c == cc:
        return "yes"

    if rr == 1 and cc == 1:
        return False

    if rr > r or cc > c:
        return False

    if rr == 0 and cc == 0:
        cell = int(room[rr][cc])

    else:
        cell = int(room[rr-1][cc-1])

    route = []

    for i in range(1, cell+1):
        if cell%i == 0:
            l = cell/i
            route.append((i,l))

    if len(route) == 0:
        return "no"

    for x in route:
        print(route)
        a = escape(int(x[0]),int(x[1]))
        if a:
            return a

    return False

value = escape(0,0)
if value == False:
    value = "no"
print(value)