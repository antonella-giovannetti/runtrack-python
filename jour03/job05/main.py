def is_prime():
    for n in range(2, 1000):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print(n)
is_prime()