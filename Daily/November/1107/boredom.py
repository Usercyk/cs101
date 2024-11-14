MAXN = int(1e5+7)
dp = [0]*MAXN
input()
for p in map(int, input().split()):
    dp[p] += p
for i in range(2, MAXN):
    dp[i] = max(dp[i-1], dp[i]+dp[i-2])
print(dp[i])
