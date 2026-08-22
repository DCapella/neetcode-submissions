class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        valid_mapping = {
            ')': '('
            ,'}': '{'
            ,']': '['
        }
        final = True
        for l in s:
            if l in valid_mapping:
                current = valid_mapping.get(l)
                if not result or result.pop() != current:
                    return False
            else:
                result.append(l)
        return len(result) == 0