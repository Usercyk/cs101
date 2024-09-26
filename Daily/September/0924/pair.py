input()
ls = sorted(map(int, input().split()))
k = int(input())
l = 0
r = len(ls)-1
res = 0
while l < r:
    if ls[l]+ls[r] < k:
        l += 1
    elif ls[l]+ls[r] > k:
        r -= 1
    else:
        res += 1
        l += 1
        r -= 1
print(res)
