import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # res = re.sub('\'|\"|-|#|@|,|:|\.|\?|\ ', '', s).lower()
        # return res == res[::-1]
        res = [i.lower() for i in s if i.isalnum()]
        return res == res[::-1]

s = Solution()
res = s.isPalindrome("A man, a plan, a canal -- Panama")
print(res)
