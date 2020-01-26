'''
执行结果：
通过
显示详情
执行用时 :
164 ms
, 在所有 Python3 提交中击败了
84.53%
的用户
内存消耗 :
28.3 MB
, 在所有 Python3 提交中击败了
31.27%
的用户
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        # 加入判空
        if not p1 or not p2:
            return None
        while p1 != p2:
            p1, p2 = p1.next, p2.next
            # 如果没有交点，则p1,p2同时指向None
            if not p1 and not p2:
                return p1

            if p1 is None: p1 = headB
            if p2 is None: p2 = headA
        return p1

# 建立节点A
a4 = ListNode(4)
a1 = ListNode(1)
a8 = ListNode(8)
a4_2 = ListNode(4)
a5_2 = ListNode(5)

# 建立节点B
a5 = ListNode(5)
a0 = ListNode(0)
a1_2 = ListNode(1)

# 将A和B节点连接，形成有交叉节点的链表
a4.next = a1
a1.next = a8
a8.next = a4_2
a4_2.next = a5_2
a5.next = a0
a0.next = a1_2
a1_2.next = a8

# 运行
headA = a4
headB = a5
s = Solution()
node = s.getIntersectionNode(headA, headB)
print(node.val)
