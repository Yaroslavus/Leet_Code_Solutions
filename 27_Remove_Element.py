"""
Given an integer array nums and an integer val, remove all occurrences of
val in nums in-place. The order of the elements may be changed. Then return
the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the
elements which are not equal to val. The remaining elements of nums are not
important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

Note that the five elements can be returned in any order.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""


# For trying in the LeetCode IDE/Web IDE:
# Remove line "from typing import..."
# Add "self" as function first argument
# Remove _NUMBER from the name of the function you want to test
from typing import List


class Solution:
    def removeElement_1(nums: List[int], val: int) -> int:
        """
        Runtime 34 ms Beats 69.8% Memory 13.8 MB Beats 49.86%

        Args:
            nums (List[int]): _description_
            val (int): _description_

        Returns:
            int: _description_
        """
        counter = len(nums) - 1
        iter = 0
        appearances = len(nums) - nums.count(val)
        while iter < counter:
            if (nums[iter] == val) and (nums[counter] != val):
                nums[iter], nums[counter] = nums[counter], nums[iter]
                counter -= 1
                iter += 1
            elif (nums[iter] == val) and (nums[counter] == val):
                counter -= 1
            elif (nums[iter] != val) and (nums[counter] == val):
                counter -= 1
                iter += 1
            elif (nums[iter] != val) and (nums[counter] != val):
                iter += 1
        return appearances, nums


class Solution:
    def removeElement_2(nums: List[int], val: int) -> int:
        """_summary_
        Runtime 23 ms Beats 99.15% Memory 13.8 MB Beats 95.15%

        Args:
            nums (List[int]): _description_
            val (int): _description_

        Returns:
            int: _description_
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter, nums