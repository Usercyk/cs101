def prefixSum(a):
    res = []
    s = 0
    for i in a:
        s += i
        res.append(s)

    return res


input()
v = tuple(map(int, input().split()))
dictionary = {1: prefixSum(v), 2: prefixSum(sorted(v))}
for _ in range(int(input())):
    t, l, r = map(int, input().split())
    print(dictionary[t][r-1]-(dictionary[t][l-2] if l > 1 else 0))
