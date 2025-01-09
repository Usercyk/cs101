def new_int(x):
    return 0 if x == "" else int(x)
def new_str(x):
    return "" if x == 0 else str(x)

m = int(input())
n = int(input())
nums = [(x, len(x)) for x in input().split()]
max_len = max(x[1] for x in nums)
nums.sort(key=lambda x: x[0]*(2*(max_len//x[1]+1)),reverse=True)
# dp[i][j]表示前i个数凑成j位的最大值
dp = [[""]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j]
        if j >= nums[i-1][1]:
            dp[i][j] = new_str(max(new_int(dp[i][j]), new_int(
                dp[i-1][j-nums[i-1][1]]+nums[i-1][0])))
print(dp[n][m])
