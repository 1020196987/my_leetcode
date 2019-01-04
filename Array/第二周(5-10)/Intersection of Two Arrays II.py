class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for item in nums1:
            if item in nums2:
                res.append(item)
                nums2[nums2.index(item)] = -1
        return res

        # res = []
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        #         nums2.remove(i)
        # return res

        # **************************
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # res = nums1_set & nums2_set
        # res_list = list(res)
        # result = []
        # for i in res_list:
        #     if nums1.count(i) > 1 and nums2.count(i) > 1:
        #         for j in range(min(nums1.count(i), nums2.count(i))):
        #             result.append(i)
        #     else:
        #         result = res_list
        # return result


s = Solution()
res = s.intersect([1, 2, 2, 1], [2, 2])
# res = s.intersect([4, 9, 5], [9, 4, 9, 8, 4])
print(res)
