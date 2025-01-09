from math import ceil
m, n, l, = int(input()), int(input()), input().split()
max_len = max(len(p) for p in l)
l.sort(key=lambda x: x*(ceil(2*max_len/len(x))), reverse=True)

weights = [len(p) for p in l]

dp = [["" for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if weights[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] +
                           l[i-1], key=lambda x: (len(x), x))
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m] if dp[n][m] else "0")
