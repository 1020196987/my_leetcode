import re

# p1 = re.compile('^[0-9]*$')
# number = p1.match("3")
# if number:
#     print("yes")
# else:
#     print("no")


# for index, item in enumerate('abcd'):
#     print(str(index)+ ' ' + item)
#
#
# print('abcd'[0:])

# if 2 in [2,4]:
#     print('aa')

# arr = [1,3,4]
# a = arr.pop(0)
# print(a)
# print(arr)

# d = 'abc'.find('f')
# print(d)
s = set()
s.add(1)
s.add(2)
s.add(1)
s.add([1, '1'])
s.add((2, '2'))
s.add((1, '1'))
print(s)
