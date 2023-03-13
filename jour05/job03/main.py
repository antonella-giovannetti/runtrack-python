n = 15
print("+" ,"-" * (n-2) ,"+")

for i in range(n-2):
    print("|", "#" * (n-3-i) + " " + "#" * i,"|")


print("+" ,"-" * (n-2) ,"+")

