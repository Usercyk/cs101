class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p = [1]*n
        for _ in range(m-1):
            for i in range(1, n):
                p[i] = p[i]+p[i-1]
        return p[-1]
