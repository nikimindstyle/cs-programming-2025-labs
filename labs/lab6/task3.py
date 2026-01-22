def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def print_primes(a, b):
    if a < 0 or a > b:
        return "Error!"
    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(str(num))
    if not primes:
        return "Error!"
    return " ".join(primes)

a = int(input())
b = int(input())
print(print_primes(a, b))