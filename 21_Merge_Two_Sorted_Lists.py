"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Uncomment to try in your IDE:
#from typing import Optional


# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def mergeTwoLists(list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        """_summary_
        Runtime 40 ms Beats 50.30% Memory 13.9 MB Beats 21.29%

        Args:
            list1 (Optional[ListNode]): head of the first linked list
            with integers
            list2 (Optional[ListNode]): head of the second linked list
            with integers

        Returns:
            Optional[ListNode]: head of the sorted linked list
        """
        output_head = slicing_tail= ListNode()
        while True:
            if list1 is None:
                slicing_tail.next = list2
                break
            if list2 is None:
                slicing_tail.next = list1
                break
            if list1.val <= list2.val:
                slicing_tail.next, list1 = list1, list1.next
            else:
                slicing_tail.next, list2 = list2, list2.next
            slicing_tail = slicing_tail.next
        return output_head.next