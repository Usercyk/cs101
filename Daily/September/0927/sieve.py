from math import sqrt


cache = {}


def eulerSieve(maxN):
    is_prime = [True] * (maxN + 1)
    is_prime[0] = is_prime[1] = False
    primes = set()
    for i in range(2, maxN + 1):
        if is_prime[i]:
            primes.add(i)
            for j in range(i * i, maxN + 1, i):
                is_prime[j] = False
    return primes


def isTPrime(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        cache[n] = False
        return False
    p = int(sqrt(n))
    if p*p != n:
        cache[n] = False
        return False
    for i in range(2, int(sqrt(p))+1):
        if p % i == 0:
            cache[n] = False
            return False
    cache[n] = True
    return True


def isSieveTPrime(n, primes):
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        cache[n] = False
        return False
    p = int(sqrt(n))
    if p*p != n:
        cache[n] = False
        return False
    if p not in primes:
        cache[n] = False
        return False
    cache[n] = True
    return True


n = int(input())
if n < 10000:
    for i in map(int, input().split()):
        print("YES" if isTPrime(i) else "NO")
else:
    primes = eulerSieve(1000000)
    for i in map(int, input().split()):
        print("YES" if isSieveTPrime(i, primes) else "NO")
