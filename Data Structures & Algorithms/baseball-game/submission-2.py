class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for op in operations:
            if op == '+':
                x = stack[-1] + stack[-2]
                total += x
                stack.append(x)
            elif op == 'D':
                x = stack[-1] * 2
                total += x
                stack.append(x)
            elif op == 'C':
                x = stack.pop()
                total -= x
            else:
                x = int(op)
                total += x
                stack.append(x)
        return total