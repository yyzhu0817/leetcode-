'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class NumArray:
    def __init__(self, nums):
        if not nums: return

        self.dp = [0] * (len(nums) + 1)
        self.dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            self.dp[i] = nums[i-1] + self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray(
["NumArray","sumRange","sumRange","sumRange"]
[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]])
param_1 = obj.sumRange(0, 5)
print(param_1)
