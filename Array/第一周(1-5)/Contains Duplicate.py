class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))



s = Solution()
res = s.containsDuplicate([1,2,3,1])
print(res)