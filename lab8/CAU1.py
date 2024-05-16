def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_twin_primes():
    for i in range(2, 1000):
        if is_prime(i) and is_prime(i + 2):
            print(f"{i} và {i + 2} là số nguyên tố sinh đôi.")
generate_twin_primes()