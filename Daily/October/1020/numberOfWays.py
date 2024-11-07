def solve():
    n = int(input())
    *a, = map(int, input().split())
    prefixSum = [a[0]]

    for i in range(1, n):
        prefixSum.append(prefixSum[i-1]+a[i])

    s = prefixSum[-1]
    if s % 3 != 0:
        return 0
    s1 = s//3
    s2=2*s1
    res=0
    tem=0
    for i in range(n):
        if i>0 and i<n-1 and prefixSum[i]==s2:
            res+=tem
        if prefixSum[i]==s1:
            tem+=1
    return res

print(solve())
