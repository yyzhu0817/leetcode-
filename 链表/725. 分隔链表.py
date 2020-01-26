'''
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
返回一个符合上述规则的链表的列表。
举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k:int):
        # 计算链表长度
        l = 0
        head = root # head后面用
        while root:
            l += 1
            root = root.next

        # 统计每个部分的个数
        part = []
        if l >= k:
            yushu = l % k
            for _ in range(k):
                part.append(l // k)
                if yushu > 0:
                    part[_] += 1
                    yushu -= 1
        else:
            for _ in range(k):
                if _  < l:
                    part.append(1)
                else:
                    part.append(0)
        print(part)

        # 对于每一个部分。。。
        result = []
        p = head
        for number in part:
            # number = 1
            for i in range(1,number):
                head = head.next
            if p:
                result.append(p)
                p = head.next
                head.next = None
                head = p
            else:
                result.append([])
        return result

    # 没有判断 k > len(链表) 的情况,还不如我自己写的
    def splitListToParts2(self, root: ListNode, k: int):
        N = 0
        cur = root
        while cur:
            N += 1
            cur = cur.next
        mod = N % k
        size = N // k
        ret = []
        cur = root

        for i in range(k):
            if cur:
                ret.append(cur)
                curSize = size + 1 if mod  > 0 else 0
                mod -= 1
                for j in range(curSize-1):
                    cur = cur.next
                next = cur.next
                cur.next = None
                cur = next
        return ret



a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a1, b1, c1, d1, e1 = ListNode(6), ListNode(7), ListNode(8), ListNode(9), ListNode(10)
a.next, b.next, c.next, d.next, e.next= b, c, d, e, a1
a1.next, b1.next, c1.next, d1.next = b1, c1, d1, e1
head = a
s = Solution()
result = s.splitListToParts2(head,11)

for n in result:
    while n:
        print(n.val)
        n = n.next
    print('--' * 20)