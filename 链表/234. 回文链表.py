'''
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        L = []
        while head:
            L.append(head.val)
            head = head.next
        return L == L[::-1]



a, b, c, d = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
a.next, b.next, c.next = b, c, d
head = a
s = Solution()
print(s.isPalindrome(head))