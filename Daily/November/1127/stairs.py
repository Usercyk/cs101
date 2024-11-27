dp = [1, 1]
n = int(input())
for _ in range(n-1):
    dp.append(dp[-1]+dp[-2])
print(dp[n])
