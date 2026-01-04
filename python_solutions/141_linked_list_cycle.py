''' ***********************************************************************************************
    * Title: 141. Linked List Cycle
    * Difficulty: Easy
    * Description: Given head, the head of a linked list, determine if the linked list has a cycle
    * in it. There is a cycle in a linked list if there is some node in the list that can be
    * reached again by continuously following the next pointer. Internally, pos is used to denote
    * the index of the node that tail's next pointer is connected to. Note that pos is not passed
    * as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
    * Source: https://leetcode.com/problems/linked-list-cycle/
    *
    * Verdict: This linked list problem turned out to be a bit more interesting than I had
    * anticipated. While using a set could work to track previous nodes, I wanted a solution that
    * not only saved on space, but also accounted for nodes that might not be unique. Therefore,
    * my solution uses two pointers that traverse the linked list, with one pointer moving twice
    * as fast as the other. If there is a cycle, the two pointers will eventually meet, and if the
    * fast pointer reaches the end of the list, then there is no cycle.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2026-1-4
    *********************************************************************************************** '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Base case: if the head is null, return False
        if not head:
            return False

        # Initialize two pointers, one moving at normal speed and the other at double speed
        ptr1, ptr2 = head, head.next

        # Iterate through the linked list until the fast pointer reaches the end
        while ptr2:
            # If the two pointers meet, a cycle exists, so return True
            if ptr1 == ptr2:
                return True

            # Move the slow pointer and fast pointer forward
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            # If the fast pointer reaches the end of the list, where it will be null, return False
            if not ptr2:
                return False
            
            # Move the fast pointer one additional step forward
            ptr2 = ptr2.next
        
        # If the while loop exits, no cycle exists, so return False
        return False
        