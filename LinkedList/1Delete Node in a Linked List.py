# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # node.val, node.next = node.next.val, node.next.next


# l = ListNode([4, 5, 1, 9])
s = Solution()
res = s.deleteNode(node=5)
print(res)
