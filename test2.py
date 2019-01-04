import sys
s = sys.stdin.readline().strip()
# s = "(((())))"
# s = "()()()()()"
# print(s)
# print(type(s))
stack = []
res = 1
for i in s:
    if i == '(':
        stack.append(i)
    else:
        res *= len(stack)
        stack.pop()
print(res)