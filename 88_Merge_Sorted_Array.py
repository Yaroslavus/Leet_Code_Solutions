"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


# For trying in the LeetCode IDE/Web IDE:
# Remove line "from typing import..."
# Add "self" as function first argument
# Remove _NUMBER from the name of the function you want to test
from typing import List


class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Args:
            nums1 (List[int]): _description_
            m (int): _description_
            nums2 (List[int]): _description_
            n (int): _description_
        """
        while n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[m + n -1] = nums2[n - 1]
            else:
                nums1[m] = nums1[m - 1]
#                nums1[m - 1] = nums2[n - 1]
                m -= 1
            n -= 1
            print(nums1)


if __name__ == "__main__":
    tests = [([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
             ([1], 1, [], 0, [1]),
             ([0], 0, [1], 1, [1]),
             ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6])]
    for nums1, m, nums2, n, ans in tests:
        print("Test: ", nums1, nums2)
        Solution.merge(nums1, m, nums2, n)
        print(nums1 == ans, nums1, '\n')