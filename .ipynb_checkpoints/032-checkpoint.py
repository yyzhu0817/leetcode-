'''
思路分析：

解题思路：

1.需有一个变量 start=-1 记录有效括号子串的起始下标，max表示最长有效括号子串长度，初始值均为0

2.遍历给字符串中的所有字符

    2.1若当前字符s[index]为左括号'('，将当前字符下标index入栈（下标稍后有其他用处），处理下一字符

    2.2若当前字符s[index]为右括号')'，判断当前栈是否为空

        2.2.1若栈为空，则start = index ，处理下一字符（当前字符右括号下标不入栈）

        2.2.2若栈不为空，则出栈（由于仅左括号入栈，则出栈元素对应的字符一定为左括号，可与当前字符右括号配对），判断栈是否为空

            2.2.2.1若栈为空，则max = max(max, index-start)

            2.2.2.2 若栈不为空，则max = max(max, index-栈顶元素值)
'''

string = '(()'
string2 = '()()'
string3 = '(()())'


class MaxParen:
	def method(self, istr):
		start = -1
		_max = 0
		stack = []
		for i, num in enumerate(istr):
			if num == '(':  # 2.1若当前字符s[index]为左括号'('，将当前字符下标index入栈（下标稍后有其他用处），处理下一字符
				stack.append(i)
			if num == ')':  # 2.2若当前字符s[index]为右括号')'，判断当前栈是否为空
				if len(stack) == 0:  # 2.2.1若栈为空，则start = index，处理下一字符（当前字符右括号下标不入栈）
					start = i
				else:  # 2.2.2若栈不为空，则出栈（由于仅左括号入栈，则出栈元素对应的字符一定为左括号，可与当前字符右括号配对），判断栈是否为空
					stack.pop()
					if len(stack) == 0:  # 2.2.2.1若栈为空，则max = max(max, index-start)
						_max = max(_max, i - start)
					else:  # 2.2.2.2若栈不为空，则max = max(max, index-栈顶元素值)
						_max = max(_max, i - stack[-1])
		return _max


a = MaxParen()
print(a.method(string))
