'''
题目描述：
假设农场中成熟的母牛每年都会生 1 头小母牛，并且永远不会死。
第一年有 1 只小母牛，从第二年开始，母牛开始生小母牛。
每只小母牛 3 年之后成熟又可以生小母牛。给定整数 N，求 N 年后牛的数量。
求：第 i 年牛的数量
'''


class Solution:
    def method(self, i):
        D = [0, 1, 2, 3]

        for y in range(4,i+1):
            D.append(y)
            D[y] = D[y - 1] + D[y - 3]
        return D[-1]


s = Solution()
print(s.method(5))
