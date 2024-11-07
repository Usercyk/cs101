# dp[M][i]表示在背包空间还剩M时从i到n-1中可以拿到的最大价值
# M<m[i]: dp[M][i]=dp[M][i+1]
# M>=m[i]: dp[M][i]=max(dp[M-m[i]][i+1]+v[i],dp[M][i+1])
# 初态dp[M][n-1]=v[n-1] if M>=m[n-1] else 0
# 待求dp[B][0]
def dp(M, i):
    global m, v, n
    if i == n-1:
        return v[n-1] if M >= m[n-1] else 0
    if M < m[i]:
        return dp(M, i+1)
    return max(dp(M-m[i], i+1)+v[i], dp(M, i+1))


n, B = map(int, input().split())
*v, = map(int, input().split())
*m, = map(int, input().split())

print(dp(B, 0))
