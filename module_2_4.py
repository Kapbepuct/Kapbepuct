numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 2:
        primes.append(i)
    for j in range(2, i):
        print(i, j)
        is_primes = i % j
        if is_primes == 0 and j < i :
            not_primes.append(i)
            break
        elif is_primes != 0 and j < i:
                primes.append(i)
print(list(set(primes)))
print(list(set(not_primes)))




