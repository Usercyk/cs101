from math import sqrt

cache = {}


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


input()
for i in map(int, input().split()):
    print("YES" if isTPrime(i) else "NO")
