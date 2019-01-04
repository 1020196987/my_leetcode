class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

s = Solution()
# res = s.strStr("hello", "ll")
res = s.strStr("aaaaa", "bba")
print(res)
