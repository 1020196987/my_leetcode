class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = []
        d_str = map(str, digits)
        digits_string = ''.join(d_str)
        digits_string2 = str(int(digits_string) + 1)
        for i in digits_string2:
            arr.append(i)
        arr2 = map(int, arr)
        return list(arr2)


s = Solution()
# res = s.plusOne([1, 2, 3])
res = s.plusOne([4, 3, 2, 1])
print(res)
