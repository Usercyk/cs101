for _ in range(int(input())):
    n = int(input())
    s = map(int, input().split())
    d = {}
    for p in s:
        if p > 2048:
            continue
        q = len(bin(p))-3
        d[q] = d.get(q, 0)+1
    for k in range(11):
        v = d.get(k, 0)
        d[k] = v - v//2 * 2
        d[k+1] = d.get(k+1, 0)+v//2
    print("YES" if d[11] > 0 else "NO")
