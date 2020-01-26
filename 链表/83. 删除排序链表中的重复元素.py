'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1 = head
        p2 = p1.next

        while p2:
            if p1.val == p2.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p1 = p2
                p2 = p2.next
        return head

a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e

head = a
while head:
    print(head.val)
    head = head.next
print('='*20)
phead = a
s = Solution()
node = s.deleteDuplicates(phead)

while node:
    print(node.val)
    node = node.next