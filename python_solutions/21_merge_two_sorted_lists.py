''' ***********************************************************************************************
    * Title: 21. Merge Two Sorted Lists
    * Difficulty: Easy
    * Description: You are given the heads of two sorted linked lists list1 and list2. Merge the
    * two lists into one sorted list. The list should be made by splicing together the nodes of the
    * first two lists. Return the head of the merged linked list.
    * Source: https://leetcode.com/problems/merge-two-sorted-lists/
    *
    * Verdict: Probably not a controversial take, but I don't particularly like problems dealing with
    * linked lists. In all my time with coding, I've never had to use one in a real-world
    * application, and while I get that the concepts behind them are important, I would rather
    * simulate a structure like a queue or stack, or anything with more practical applications.
    * Back to the problem, this one is a textbook linked list problem, and even though I did find
    * it a bit challenging to keep the correct list state intact, it was overall nothing to write
    * home about. Also Happy New Year, since this is my first problem of 2026!
    * Language: Python
    * Time Complexity: O(n+m)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2026-1-4
    *********************************************************************************************** '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy start node and an overall result node to build the merged list
        start = result = ListNode()

        # Iterate through both lists while neither is empty
        while list1 and list2:
            # If the current node in list1 is smaller, append it to the merged list and move to the
            # next value in list1
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            # Else, perform the steps above on list2
            else:
                result.next = list2
                list2 = list2.next
            # Move the result pointer to the newly added node
            result = result.next
        
        # Once one of the lists is empty, append the remainder of the other list to the merged list
        if list1:
            result.next = list1
        else:
            result.next = list2  

        # Finally, return the merged list, which starts at start.next to skip the dummy node      
        return start.next