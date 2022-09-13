# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for char in s:
            if char in d:
                if len(stack) == 0:
                    stack.append(char)
                else:
                    if d[char] != stack[-1]:
                        stack.append(char)
                    else:
                        stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

print(Solution().isValid("(){}[]"))