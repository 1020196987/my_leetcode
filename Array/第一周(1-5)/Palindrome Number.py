class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
        x = str(x)
        x_num = len(x)
        if x_num % 2 == 0:
            index = len(x) / 2
        else:
            index = len(x) / 2 + 1
        index = int(index)
        print(index)
        return x[:index] == x[: index-1:-1]

        # print(index)
        print(x[:index])
        print(x[: index-1:-1])
        # return str(x) == str(x)[::-1]
        # """
        # :type x: int
        # :rtype: bool
        # """
        # x = str(x)
        # y = x[::-1]
        # if x == y:
        #     return True
        # else:
        #     return False


s = Solution()
res = s.isPalindrome(10)
print(res)
