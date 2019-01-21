# **********************************************
# class MinStack:
#
#     def __init__(self):
#         self.q = []
#
#     # @param x, an integer
#     # @return an integer
#     def push(self, x):
#         curMin = self.getMin()
#         if curMin == None or x < curMin:
#             curMin = x
#         self.q.append((x, curMin))  # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#
#     # @return nothing
#     def pop(self):
#         self.q.pop()
#
#     # @return an integer
#     def top(self):
#         if len(self.q) == 0:
#             return None
#         else:
#             return self.q[len(self.q) - 1][0]
#
#     # @return an integer
#     def getMin(self):
#         if len(self.q) == 0:
#             return None
#         else:
#             return self.q[len(self.q) - 1][1]
#
#     def display(self):
#         print(self.q)


# # ****************************************



# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.stack.pop()
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return min(self.stack)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(4)
obj.push(3)
obj.push(10)
# obj.display()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
