# dp[H][i] 表示在H限制下，从i到n-1中可以拦下最多多少个
# if H<h[i]: dp[H][i]=dp[H][i+1]
# if H>=h[i]: dp[H][i]=max(dp[h[i]][i+1]+1, dp[H][i+1])
# 初态：dp[H][n-1]=1 if H>=h[n-1] else 0
# 问题：dp[MAXH][0]
def dp(H, i):
    global h, n
    if i == n-1:
        return 1 if H >= h[n-1] else 0
    if H < h[i]:
        return dp(H, i+1)
    return max(dp(h[i], i+1)+1, dp(H, i+1))


n = int(input())
*h, = map(int, input().split())
print(dp(max(h), 0))
