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

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0 
    j = 0 
    k = l 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r: 
  
        m = int((l+(r-1))/2)

        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  


mergeSort(coordinatesx,0,int(len(coordinatesx)-1))
mergeSort(coordinatesy,0,int(len(coordinatesy)-1))
print(str(coordinatesx[0]-1) + "," + str(coordinatesy[0]-1))
print(str(coordinatesx[len(coordinatesx)-1]+1) + "," + str(coordinatesy[len(coordinatesy)-1]+1))