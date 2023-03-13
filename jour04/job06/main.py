def list_fruits():
    fruits=['pomme', 'cerise', 'orange', 'melon']
    swap = fruits[-1]
    fruits[-1] = fruits[0]
    fruits[0] = swap
    return fruits

print(list_fruits())