s = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1
i = 0

while i + n <= len(s):
    print(s[i:i+n])
    i += n
    n += 2
