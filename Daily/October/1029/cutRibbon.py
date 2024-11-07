# dp[i][j]表示考虑前i件物品，长度为j的丝带可以分多少段
# dp[i-1][j]=max(dp[i-1][j],dp[i][j-w[i]]+1)
# 初态dp[i][0]=0, dp[0][j]=0
# 待求dp[3][n]
# 要求必须装满背包

dp = [-1]*4100
dp[0] = 0
n, *w = map(int, input().split())

for i in range(3):
    for j in range(w[i], n+1):
        if dp[j-w[i]] != -1:
            dp[j] = max(dp[j], dp[j-w[i]]+1)

print(dp[n])
