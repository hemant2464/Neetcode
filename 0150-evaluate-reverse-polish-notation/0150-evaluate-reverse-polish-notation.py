class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        [stack.append(int(c)) if c not in "+-*/" else stack.append(int(eval(str(stack.pop(-2)) + c + str(stack.pop())))) for c in tokens]
        return stack[0]