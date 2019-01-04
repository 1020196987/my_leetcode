class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 第一种方法：
        # for i in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)
        # nu = nums
        # return nu
        # 第二种方法：
        #     arr = []
        #     for i in range(k):
        #         temp = nums.pop()
        #         arr.append(temp)
        #     arr.reverse()
        #     arr.extend(nums)
        #     # nums.clear()
        #     # nums = arr
        #     return arr
        # [nums.insert(0, item) for index, item in enumerate(nums)]
        # 第三种方法
        #     length = len(nums)
        #     if length == 1 or k == 0:
        #         nums[:] = nums
        #         return nums
        #     else:
        #         temp = nums[-k:]
        #         temp.extend(nums[:length-k])
        #         # nums.clear()
        #         nums[:] = temp
        #         return nums
        # return nums[-k:].extend(nums[:k])
        # return a
        # 第四种写法
        # nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
        # arr = []
        #
        # return nums

        arr = [1, 3, 5]
        nums2 = arr
        nums[:] = arr
        print(id(nums2))
        print(id(arr))
        print(id(nums))


s = Solution()
# res = s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
res = s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
# print(res)
