from bisect import bisect


n = int(input())
a = sorted(map(int, input().split()))
for _ in range(int(input())):
    m = int(input())
    print(bisect(a, m))
