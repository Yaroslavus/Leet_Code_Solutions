"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false

Example 3:

Input: x = 10
Output: false

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


# For trying in the LeetCode IDE/Web IDE:
# Add "self" as function first argument
# Remove _NUMBER from the name of the function you want to test


class Solution:
    def isPalindrome_1(x: int) -> bool:
        """_summary_
        Runtime 76 ms Beats 19.53% Memory 13.9 MB Beats 7.93%

        Args:
            x (int): integer (123, 454, -345, 1)

        Returns:
            bool: Palindrom or not
        """
        if x < 0:
            return False
        reversed_x = 0
        temp = x
        while temp:
            reversed_x = reversed_x*10 + temp%10
            temp //= 10
        return x == reversed_x


class Solution:
    def isPalindrome_2(x: int) -> bool:
        """_summary_
        Runtime 71 ms Beats 32.70% Memory 13.8 MB Beats 46.86%

        Args:
            x (int): integer (123, 454, -345, 1)

        Returns:
            bool: Palindrom or not
        """
        l = []
        while x:
            l.append(x%10)
            x //= 10
        return l == l[::-1]