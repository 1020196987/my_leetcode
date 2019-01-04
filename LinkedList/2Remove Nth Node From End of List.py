# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 第一种思路，本地没有问题，但是线上有问题
    def removeNthFromEnd(self, head, n):

    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     count = 0
    #     p = head
    #     while p.next:
    #         count += 1
    #         p = p.next
    #     if count == 1 and n >= 1:
    #         return None
    #     # 把第count-n+1个删除
    #     p = head
    #     for i in range(count - n - 1):
    #         p = p.next
    #     if n != 0:
    #         p.next = p.next.next
    #     return head
    # *****************************************************

        cur = pre = head
        for _ in range(n):
            cur = cur.next
        if not cur:
            return head.next
        while cur.next:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return head

h = ListNode(1)
point = h
n = 5
for i in range(n):
    curr = ListNode(i + 2)
    point.next = curr
    point = curr
point = h
while point.next:
    # print(point.val)
    point = point.next
s = Solution()
res = s.removeNthFromEnd(h, 2)
point = res
if point == None:
    print(None)
else:
    while point.next:
        print(point.val)
        point = point.next
