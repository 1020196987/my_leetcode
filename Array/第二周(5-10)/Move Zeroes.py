class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # length = len(nums)
        # for i in range(length):
        #     if nums[i] == 0:
        #         nums.append(nums[i])
        #         nums.remove(nums[i])
        # return nums


        # 优化
        # *********************************************

        # for i in range(len(nums)):
        #     temp = nums[i]
        #     if temp == 0:
        #         nums.append(temp)
        #         nums.remove(temp)
        # return nums

        # 再优化
        # *********************************************
        arr = []
        for i in nums:
            if i != 0:
                arr.append(i)
        print(arr)
        for i in range(len(nums) - len(arr)):
            arr.append(0)
        nums[:] = arr[:]
        return nums

s = Solution()
res = s.moveZeroes([0, 1, 0, 3, 12])
print(res)
