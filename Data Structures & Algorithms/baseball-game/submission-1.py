class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        i = 0
        for op in operations:
            if op == '+':
                x = stack[i-1] + stack[i-2]
                total += x
                stack.append(x)
                i += 1
            elif op == 'D':
                x = stack[i-1] * 2
                total += x
                stack.append(x)
                i += 1
            elif op == 'C':
                x = stack.pop()
                total -= x
                i -= 1
            else:
                x = int(op)
                total += x
                stack.append(x)
                i += 1
        return total