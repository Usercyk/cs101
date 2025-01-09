names = ["A", "B", "C"]


def hanoi(n, p, q):
    if n == 1:
        print(f"{names[p]}->{names[q]}")
        return
    hanoi(n-1, p, 3-p-q)
    print(f"{names[p]}->{names[q]}")
    hanoi(n-1, 3-p-q, q)


n = int(input())
print(2**n-1)
hanoi(n, 0, 2)
