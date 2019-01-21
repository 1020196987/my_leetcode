class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用来维护局部最优解和全局最优解
        local_v, global_v = nums[0], nums[0]
        for v in nums[1:]:
            local_v = max(v+local_v, v)
            global_v = max(local_v, global_v)
        return global_v


s = Solution()
res = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
