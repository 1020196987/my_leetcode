from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for i, v in enumerate(s):
        #     t_index = t.find(v)
        #     if t_index != -1:
        #         t = t.replace(t[t_index], '0', 1)
        #     s = s.replace(s[i], '0', 1)
        #
        # return s == t

        return Counter(s) == Counter(t)


s = Solution()
# res = s.isAnagram("anagram", "nagaram")
res = s.isAnagram("rat", "car")
print(res)
