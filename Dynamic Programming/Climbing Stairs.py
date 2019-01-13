class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 1:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # dp = [0] + [1] + [2] + [0] * (n - 2)
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]


s = Solution()
res = s.climbStairs(4)
print(res)
