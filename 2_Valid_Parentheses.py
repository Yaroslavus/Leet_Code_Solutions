class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {'(': ')', '[': ']', '{': '}'}
        for symbol in s:
            if symbol in brackets_dict:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if symbol != brackets_dict[left]:
                    return False
        return len(stack) == 0