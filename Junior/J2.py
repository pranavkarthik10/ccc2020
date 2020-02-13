p = int(input())
n = int(input())
r = int(input())

d = 0

l = n
while l < p+1:
    d+=1
    n = n*r
    l += n
print(d)
