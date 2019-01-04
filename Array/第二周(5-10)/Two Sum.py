class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for index, item in enumerate(nums):
        #     leave = target - item
        #     try:
        #         leave_index = nums.index(leave)
        #     except ValueError:
        #         leave_index = -1
        #
        #     if leave in nums and leave_index != -1 and leave_index != index:
        #         return [index, leave_index]

        # *********************************************************
        # for k, item in enumerate(nums):
        #     leave = target - item
        #     # if leave in nums[k:]:
        #     for i, con in enumerate(nums[k+1:]):
        #         if con == leave:
        #             leave_index = i+k+1
        #             return [k, leave_index]
        # *********************************************************
        # try:
        #     leave_index = nums.index(leave)
        # except ValueError:
        #     leave_index = -1
        #
        # if leave in nums and leave_index != k and leave_index != -1:
        #     return [k, leave_index]

        # *********************************************************
        # for k, item in enumerate(nums):
        #     leave = target - item
        #     if leave in nums[k + 1:]:
        #         return [k, nums[k + 1:].index(leave) + k + 1]
        # *********************************************************
        # nums_dict = {}
        # for index, item in enumerate(nums):
        #     nums_dict[item] = index
        # print(nums_dict)
        # # for index, item in enumerate(nums):
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], index]
            dict[num] = index
        #     print(dict)

s = Solution()
res = s.twoSum([3, 4, 3], 6)
print(res)
