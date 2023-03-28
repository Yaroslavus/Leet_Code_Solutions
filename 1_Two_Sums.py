"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime 67 ms Beats 57.46% Memory 15.4 MB Beats 5.96%
        Args:
            nums (List[int]): _description_
            target (int): _description_

        Returns:
            List[int]: _description_
        """
        d,target_list = {}, []
        for i, item in enumerate(nums):
            if item not in d.keys():
                d[item] = i
            else:
                if item*2 == target:
                    return [d[item], i]
        if not target%2 and target/2 in d.keys():
            del d[target//2]
        nums_diff = [target - item for item in nums]
        for item in nums_diff:
            if item in d.keys():
                target_list.append(d[item])
        return sorted(target_list)