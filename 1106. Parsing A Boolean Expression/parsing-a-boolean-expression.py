class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        i = 0
        
        while i < len(expression):
            char = expression[i]
            
            if char == 't':
                stack.append(True)
            elif char == 'f':
                stack.append(False)
            elif char in '!&|':
                stack.append(char)
            elif char == '(':
                # Push the current operator to the stack
                stack.append(char)
            elif char == ')':
                # Start processing until we hit the corresponding '('
                sub_expr = []
                while stack and stack[-1] != '(':
                    sub_expr.append(stack.pop())
                sub_expr.reverse()  # Reverse to get the correct order
                stack.pop()  # Remove the '('

                # The last element before '(' is the operator
                operator = stack.pop()
                if operator == '!':
                    result = not sub_expr[0]  # Apply NOT
                elif operator == '&':
                    result = all(sub_expr)  # Apply AND
                elif operator == '|':
                    result = any(sub_expr)  # Apply OR

                stack.append(result)  # Push the result back onto the stack

            i += 1
        
        # The result should be the only item left on the stack
        return stack[0]
