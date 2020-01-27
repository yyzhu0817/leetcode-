'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1],

]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        D = [[0 for _ in range(n)] for _ in range(m)]
        # 边界处理，列
        sum = 0
        for j in range(n):
            sum += grid[0][j]
            D[0][j] = sum
        # 边界处理，行
        sum = 0
        for i in range(m):
            sum += grid[i][0]
            D[i][0] = sum
        # 其他情况
        for i in range(1, m):
            for j in range(1, n):
                D[i][j] = grid[i][j] + min(D[i - 1][j], D[i][j - 1])
        return D[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution()
print(s.minPathSum(grid))
