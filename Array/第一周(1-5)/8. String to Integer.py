import re


def take_sign(str):
    is_minus_sign = False
    str2 = str
    for index, item in enumerate(str):
        if item == '-' or item == '+':
            str2 = str[index + 1:]
            str = str2
            if item == '-':
                is_minus_sign = True
        else:
            val = is_start_num(str2, is_minus_sign)
            return val
    is_start_num(str2, is_minus_sign)


def is_start_num(str, flag):
    num = ''
    for index, item in enumerate(str):
        if (re.compile('^[0-9]$').match(item)):
            num += item
        else:
            break
    if len(num) == 0:
        return 0
    else:
        if flag:
            is_minus_sign = False
            if -int(num) < - 2 ** 31:
                return (-2 ** 31)
            else:
                return (-int(num))
        else:
            if int(num) > 2 ** 31 - 1:
                return (2 ** 31 - 1)
            else:
                return (int(num))


class Solution:
    def __init__(self):
        self.is_minus_sign = False

    def myAtoi(self, str):
        if str == "" or str == '-' or str == '+':
            return 0
        str2 = str
        for index, item in enumerate(str):

            if item == ' ':
                str2 = str[index + 1:]
            else:
                val = take_sign(str2)
                return val
            if index + 1 >= len(str):
                return 0
        take_sign(str2)


s = Solution()
val = s.myAtoi(" -42")
print(val)
