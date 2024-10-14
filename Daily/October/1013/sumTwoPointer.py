n, k = map(int, input().split())
*a, = map(int, input().split())
i = 0
j = n-1
res = 0
while i < j:
    if a[i]+a[j] < k:
        i += 1
        continue
    if a[i]+a[j] > k:
        j -= 1
        continue
    res += 1
    i += 1
    j -= 1
print(res)
