class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        arr.append(2)
        x = arr.pop()
        print(x)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) <= 2:
            return max(nums[0], nums[-1])
        sum_money = [0] * len(nums)
        sum_money[0], sum_money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            sum_money[i] = max(nums[i] + sum_money[i - 2], sum_money[i - 1])
        return sum_money[len(nums) - 1]


s = Solution()
res = s.rob([1, 2, 3, 1])
print(res)



