n = int(input())

for _ in range(n):
    a = int(input())
    print("YES" if a.bit_count() != 1 else "NO")