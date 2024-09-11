from math import sqrt


def isPrime(p):
    for i in range(3, int(sqrt(p))+1):
        if p % i == 0:
            return False
    return True


def main():
    x = int(input())
    if x < 6 or x % 2 == 1:
        print("Error!")
        return
    for i in range(3, x//2+1, 2):
        if isPrime(i) and isPrime(x-i):
            print(f"{x}={i}+{x-i}")


main()
