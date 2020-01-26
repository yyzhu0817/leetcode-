'''
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
进阶: 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:
输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 转换成整数求和，再转化为链表
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum1 = 0
        sum2 = 0
        while l1:
            sum1 = sum1*10 + l1.val
            l1 = l1.next
        while l2:
            sum2 = sum2*10 + l2.val
            l2 = l2.next
        sum = sum1 + sum2
        head = ListNode(sum%10)
        sum = sum // 10
        while sum != 0:
            n = sum % 10
            temp = ListNode(n)
            temp.next = head
            head = temp
            sum = sum // 10
        return head



a, b, c, d = ListNode(7), ListNode(2), ListNode(4), ListNode(3)
x, y, z = ListNode(5), ListNode(6), ListNode(4)
a.next = b
b.next = c
c.next = d
x.next, y.next = y, z
l1 = a
l2 = x

s = Solution()
head = s.addTwoNumbers(l1,l2)
while head:
    print(head.val)
    head = head.next
