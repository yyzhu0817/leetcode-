'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 递归
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1.终止条件
        if not head or not head.next:
            return head

        # 2. 单次过程
        p = head.next
        head.next = self.swapPairs(p.next)
        p.next = head

        # 3.找返回值
        return p

    # 法2:建立哨兵节点
    def swapPairs2(self, head: ListNode) -> ListNode:
        first = ListNode(0)
        first.next = head
        p1 = first
        while p1.next and p1.next.next:
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1.next.next
            p1.next.next = p2
            p1 = p2
        return first.next




a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

head = a
while head:
    print(head.val)
    head = head.next

print('=' * 20)

s = Solution()
phead = a
node = s.swapPairs2(phead)
while node:
    print(node.val)
    node = node.next
