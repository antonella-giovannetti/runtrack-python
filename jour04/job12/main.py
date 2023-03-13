L = [7, 11, 42, 39, 2]

count = 0
for i in L:
    count +=1

def sortNumber(L):
    for i in range(count):
        for j in range(0, count-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


print(sortNumber(L))