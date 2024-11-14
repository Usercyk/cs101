# dp[i][1]表示i前摆动序列上升结尾中最长的
# dp[i][0]表示i后摆动序列下降结尾中最长的
# nums[i-1]<num[i]: dp[i][0]=dp[i-1][0];dp[i][1]=max(dp[i-1][1],dp[i-1][0]+1)
# nums[i-1]>num[i]: dp[i][1]=dp[i-1][1];dp[i][0]=max(dp[i-1][0],dp[i-1][1]+1)
# dp[0][0]=dp[0][1]=1
# ans=max(dp[n-1][0], dp[n-1][1])

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp = [1, 1]
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            s = nums[i] > nums[i-1]
            dp[1-s] = max(dp[1-s], dp[s]+1)
        return max(dp)
