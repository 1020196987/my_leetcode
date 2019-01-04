# class Solution:
#
#     def removeDuplicates(self, nums):
#         nums_set = set(nums)
#         length = len(nums_set)
#         for i in range(len(nums)):
#             nums.pop()
#         for i in nums_set:
#             nums.append(i)
#         nums.sort()
#         return length
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0

        len_nums = len(nums)
        if len_nums > 0:

            prev_v = nums[0]
            length = 1

            for i in range(1, len_nums):
                if nums[i] != prev_v:
                    prev_v = nums[length] = nums[i]
                    # print(nums[length])
                    # print('aa')
                    # print(nums[i])
                    length += 1
            print(length)
            print(len_nums)
            del nums[length:len_nums]
            print(nums)
        return length


s = Solution()
l = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(l)
