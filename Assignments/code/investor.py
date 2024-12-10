*a, = map(int, input().split())
n = len(a)
inf = 1000000
sup = -10000
res_inf = []
res_sup = []
for i in range(n):
    inf = min(a[i], inf)
    res_inf.append(inf)

    sup = max(a[n-1-i], sup)
    res_sup.append(sup)

res_sup.reverse()

money = max((res_sup[i]-res_inf[i] for i in range(n)))
print(max(money, 0))
