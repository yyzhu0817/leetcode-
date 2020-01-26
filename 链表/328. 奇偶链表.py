'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''
import time
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 奇偶初始化
        odd = head
        if head:
            even = head.next
        else:
            return head
        T = even

        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = T
        return head

# 实例
a, b, c, d, e = ListNode(2), ListNode(1), ListNode(3), ListNode(5), ListNode(6)
a1, b1 = ListNode(4), ListNode(7)
a.next, b.next, c.next, d.next, e.next= b, c, d, e, a1
a1.next = b1
head = a

start = time.time()
s = Solution()
listNode = s.oddEvenList(head)
while listNode:
    print(listNode.val)
    listNode = listNode.next
end = time.time()
print(f'用时:{1000*(end-start)}ms')
