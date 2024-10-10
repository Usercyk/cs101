input()
a = sorted(map(int, input().split()))
wait = 0
res = 0
for p in a:
    if p >= wait:
        res += 1
        wait += p
print(res)
