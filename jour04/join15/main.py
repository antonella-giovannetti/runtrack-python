L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def length(el):
    count = 0
    for i in el:
        count+=1
    return count

for i in range(length(L)):
    # récuperer la partie entiere
    integer_part = int(L[i])
    # récuperer la partie decimal
    decimal_part = L[i] - integer_part

    # arrondir la partie décimale à l'entier le plus proche
    if decimal_part >= 0.5:
        integer_part += 1
    
    # mettre à jour le nombre dans la liste
    L[i] = integer_part



print(L)