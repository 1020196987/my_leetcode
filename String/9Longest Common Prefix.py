class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if len(strs) == 0:
        #     return ''
        # if len(strs) == 1:
        #     return strs[0]
        # first = strs[0]
        # count = 0
        # # print(min(strs, key=lambda x: len(x)))
        # for index in range(0, len(min(strs, key=lambda x: len(x)))):
        #     for j in range(1, len(strs)):
        #         # try:
        #         temp = strs[j][index]
        #         # except IndexError:
        #         #     temp = ''
        #         if temp == first[count]:
        #             if j + 1 == len(strs):
        #                 count += 1
        #         else:
        #             return first[:count]
        # return first[:count]


        # **************************************************
        # 第二种方式
        if not strs:
            return ""
        print(list(zip("flower", "flow", "flight")))
        print(list(zip(*strs)))
        for i, words in enumerate(zip(*strs)):
            if len(set(words)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
s = Solution()
# res = s.longestCommonPrefix(["c", "acc", "ccc"])
res = s.longestCommonPrefix(["flower", "flow", "flight"])
print(res)
