def primes(max):
    prime = []
    for n in range(1, max + 1, 2):
        f = 0
        is_prime = True
        for i in prime:
            if n % i == 0:
                is_prime = False
                break
            if i * i > n:
                break
        if is_prime:
            prime.append(n)
    return prime


print(primes(1000))