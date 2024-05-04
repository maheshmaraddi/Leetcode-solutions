class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+","-","*","/"]
        for t in tokens:
            if t not in op:
                stack.append(t)
            else:
                b=int(stack.pop())
                a=int(stack.pop())
                if t == "+":
                    stack.append(b+a)
                elif t =="-":
                    stack.append(a-b)
                elif t== '*':
                    stack.append(a*b)
                elif t == "/":
                    res = round(int(a/b))
                    stack.append(res)
        return int(stack[0])
                

        