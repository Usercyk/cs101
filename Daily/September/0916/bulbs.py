n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.update(list(map(int, input().split()))[1:])

if s == set(range(1, m+1)):
    print("YES")
else:
    print("NO")
