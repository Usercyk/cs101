n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = sorted(map(int, input().split()))
res = 0
i = 0
j = 0
while i < n and j < m:
    if a[i]-1 <= b[j] <= a[i]+1:
        res += 1
        i += 1
        j += 1
        continue
    if a[i] < b[j]:
        i += 1
        continue
    j += 1
print(res)
