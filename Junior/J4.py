t = input()
s = input()

out = "no"

cyclic = []
cyclic.append(s)
for i in range(len(s)-1):
    x = list(cyclic[i])
    temp = x[0]
    for l in range(1, len(x)):
        x[l-1] = x[l]
    x[len(x)-1] = temp
    x = "".join(x)
    cyclic.append(x)

if len(s) < len(t)+1:

    for i in range(len(t)-len(s)+1):
        check = ""
        for x in range(len(s)):
            check += t[i+x]
        for l in cyclic:
            if check == l:
                out = "yes"
print(out)