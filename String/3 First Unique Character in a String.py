class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len == 1:
            return 0
        for i in range(s_len):

            if s[i] == '0':
                continue
            elif s[i] not in s[i + 1:]:
                return i
            else:
                s = s.replace(s[i], '0', s.count(s[i]))
        return -1
#
# class Solution:
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 1:
#             return 0
#         for key, item in enumerate(s):
#             s_s = s[key + 1:]
#             if item not in s_s and key != len(s) - 1:
#                 return key
#             elif item == '0':
#                 continue
#             else:
#                 s = s.replace(item, '0', s.count(item))
#         return -1
s = Solution()
res = s.firstUniqChar("aadadaad")
print(res)
