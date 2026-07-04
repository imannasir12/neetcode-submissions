class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if not char in mapping:
                stack.append(char)
            else:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack
        