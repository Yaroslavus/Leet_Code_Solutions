"""
Write a function to find the longest common prefix string
amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """_summary_
        Runtime 34 ms Beats 72.61% Memory 13.8 MB Beats 79.11%
        Args:
            strs (List[str]): List of strings

        Returns:
            str: the longest common prefix
        """
        min_word = min(strs, key=len)
        for i in range(len(min_word), 0, -1):
            flag = all([min_word[:i] == word[:i] for word in strs])
            if flag:
                return min_word[:i]
        return ""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """_summary_
        Runtime 35 ms Beats 66.66% Memory 13.9 MB Beats 38.28%
        Args:
            strs (List[str]): List of strings

        Returns:
            str: the longest common prefix
        """
        strs.sort()
        min_word = strs[0]
        last_word = strs[-1]
        i = 0
        while i < len(min_word) and min_word[i] == last_word[i]:
            i += 1
        return min_word[:i]