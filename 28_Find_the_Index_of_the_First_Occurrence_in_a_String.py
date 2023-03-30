"""
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """_summary_
        Runtime 29 ms Beats 77.78% Memory 13.8 MB Beats 94.84%

        Args:
            haystack (str): string where we search
            needle (str): target string to find in haystack

        Returns:
            int: index of the first occurance of
            the needle in the haystack
        """
        needle_length = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + needle_length] == needle:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """_summary_
        Runtime 30 ms Beats 74.22% Memory 13.8 MB Beats 51.56%

        Args:
            haystack (str): string where we search
            needle (str): target string to find in haystack

        Returns:
            int: index of the first occurance of
            the needle in the haystack
        """
        if needle in haystack:
            return haystack.index(needle)
        return -1


"""
YOU CAN ALSO USE:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

Runtime 34 ms Beats 45.7% Memory 13.8 MB Beats 94.84%

OR

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        return -1

Runtime 39 ms Beats 13.40% Memory 13.9 MB Beats 51.56%

BUT STR.FIND works slower than STR.INDEX
"""