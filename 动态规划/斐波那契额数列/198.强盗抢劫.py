'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''


class Solution:

    def rob0(self, nums):
        sum1 = 0
        sum2 = 0
        for i in range(0, len(nums), 2):  # i指定所有奇数
            sum1 += nums[i]
            sum1 = max(sum1,sum2)
            if i + 1 < len(nums):
                sum2 += nums[i + 1]
                sum2 = max(sum1,sum2)
        return max(sum1, sum2)

    # 动态规划大法
    def rob(self, nums):
        dp = []
        if len(nums) == 0: return 0
        dp.append(nums[0])  # dp[0]
        if len(nums) == 1: return dp[0]
        dp.append(max(nums[0], nums[1])) # dp[1]
        if len(nums) == 2: return dp[1]

        for i in range(2, len(nums)):
            first = dp[i - 2] + nums[i]
            second = dp[i - 1]
            dp.append(max(first, second))
        return dp[len(nums) - 1]


nums = [2,1,1,2]
s = Solution()
print(s.rob0(nums))
