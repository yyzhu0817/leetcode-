class Solution:
    def twoSum(self, number, target):
        if number is None:
            return None

        i = 0
        j = len(number) - 1
        while i < j:
            if number[i] + number[j] < target and i < j:
                i += 1
            elif number[i] + number[j] > target and i < j:
                j -= 1
            else:
                return [i + 1, j + 1]


s = Solution()
numbers = [3,24,50,79,88,150,345]
target = 200
print(s.twoSum(numbers, target))
