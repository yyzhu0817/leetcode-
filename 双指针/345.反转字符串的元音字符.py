'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        yuanYinZifu = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = [i for i in s]
        i = 0
        j = len(l) - 1
        while i < j:
            while l[i] not in yuanYinZifu and i < j:
                i += 1
            while l[j] not in yuanYinZifu and i < j:
                j -= 1
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return ''.join(l)


s = Solution()
print(s.reverseVowels('leetcode'))
