class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 第一种方式：
        # x = str(x)
        # if x[0] == '-':
        #     res = x[1:]
        #     res = '-' + res[::-1]
        #     res = int(res)
        #     if res < -2 ** 31 or res > 2 ** 31:
        #         return 0
        #     else:
        #         return int(res)
        #
        # else:
        #     res = int(x[::-1])
        #     if res < -2 ** 31 or res > 2 ** 31:
        #         return 0
        #     else:
        #         return res
        # **********************************************
        # 第二种方式：
        if x < 0:
            res = str(x)[::-1][:-1]
            res = int('-' + res)
            if res < -2 ** 31 or res > 2 ** 31:
                return 0
            else:
                return res
        else:
            res = int(str(x)[::-1])
            if res < -2 ** 31 or res > 2 ** 31:
                return 0
            else:
                return res


s = Solution()
res = s.reverse(120)
print(res)
