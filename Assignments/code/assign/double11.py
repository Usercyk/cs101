def dfs(pur, costs):
    global n, ans, m
    if pur > n:
        zhekou = [0]*m
        for i in range(m):
            for k in shops[i].keys():
                if costs[i] >= k:
                    zhekou[i] = max(zhekou[i], shops[i][k])
        total = sum(costs)
        total -= total//300*50
        total -= sum(zhekou)
        ans = min(ans, total)
        return
    shoppable = purchase[pur]
    for shop, cost in shoppable.items():
        costs[shop-1] += cost
        dfs(pur+1, costs)
        costs[shop-1] -= cost


n, m = map(int, input().split())
shops = []
shops_keys = []
purchase = [{}]
for i in range(n):
    s = input().split()
    d = {}
    for p in s:
        a, b = map(int, p.split(":"))
        d[a] = b
    purchase.append(d)
for _ in range(m):
    s = input().split()
    d = {}
    for p in s:
        a, b = map(int, p.split("-"))
        d[a] = b
    shops.append(d)

ans = float("inf")
dfs(1, [0]*m)
print(ans)
