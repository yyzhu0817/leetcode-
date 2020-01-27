'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        D = [[1 for _ in range(n)] for __ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                D[i][j] = D[i][j-1] + D[i-1][j]
        return D

    def uniquePaths2(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre

s = Solution()
print(s.uniquePaths2(3,2))
'''
执行结果：通过
显示详情 执行用时 :32 ms, 在所有 Python3 提交中击败了82.86%的用户
内存消耗 :12.9 MB, 在所有 Python3 提交中击败了61.48%的用户
'''