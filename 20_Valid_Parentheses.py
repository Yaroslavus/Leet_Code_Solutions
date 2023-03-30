"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


# For trying in the LeetCode IDE/Web IDE:
# Add "self" as function first argument


class Solution:
    def isValid(s: str) -> bool:
        """_summary_
        Runtime 20 ms Beats 99.21% Memory 13.8 MB Beats 59.22%
        Args:
            s (str): some sequence of symbols {[()]}

        Returns:
            bool: True or False - is a valid bracket sequence
        """
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