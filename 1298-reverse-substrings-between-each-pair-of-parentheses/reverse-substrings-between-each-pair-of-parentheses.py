class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c==")":
                word= []
                while  stack[-1]!="(":
                    word.append(stack.pop())
                stack.pop()
                stack.extend(word)
            else:
                stack.append(c)

        return ''.join(stack)