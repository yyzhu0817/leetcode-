'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, pre = head, None
        while p:
            temp = p.next
            p.next = pre
            pre = p
            p = temp
        head = pre
        return head

_1 = ListNode(1)
_2 = ListNode(2)
_3 = ListNode(3)
_4 = ListNode(4)
_5 = ListNode(5)

head = _1
_1.next = _2
_2.next = _3
_3.next = _4
_4.next = _5

p = head
while p:
    print(p.value)
    p = p.next
print('='*30)
s = Solution()
reverse_s = s.reverseList(head)


while reverse_s:
    print(reverse_s.value)
    reverse_s = reverse_s.next