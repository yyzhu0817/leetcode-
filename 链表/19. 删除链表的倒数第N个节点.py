'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = head
        p = head

        for _ in range(n):
            if p.next:
                p = p.next
            else:
                return head.next
        while p.next:
            pre = pre.next
            p = p.next
        pre.next = pre.next.next
        return head


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
print('='*20)

s = Solution()
phead = a
node = s.removeNthFromEnd(phead,5)

while node:
    print(node.val)
    node = node.next