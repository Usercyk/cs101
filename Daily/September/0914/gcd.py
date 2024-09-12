from math import gcd
while True:
    try:
        print(gcd(*map(int, input().split())))
    except EOFError:
        break
