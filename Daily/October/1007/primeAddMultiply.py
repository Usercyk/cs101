from math import sqrt


def isPrime(x):
    for p in range(2, int(sqrt(x))+1):
        if x % p == 0:
            return False
    return True


s = int(input())
if s % 2 == 1:
    print(2*(s-2))
else:
    for i in range(s//2 if s//2 % 2 == 1 else s//2-1, 3, -2):
        if not (isPrime(i) and isPrime(s-i)):
            continue
        print(i*(s-i))
        break
