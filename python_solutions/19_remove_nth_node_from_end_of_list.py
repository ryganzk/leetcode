''' ***********************************************************************************************
    * Title: 19. Remove Nth Node From End of List
    * Difficulty: Medium
    * Description: Given the head of a linked list, remove the nth node from the end of the list
    * and return its head.
    * Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    *
    * Verdict: A relatively simple problem overall, the only area I found tricky was handling lists
    * with only one node. My workaround was to use a dummy node at the start of the list that would
    * allow me to avoid edge cases when removing the head node. 
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2026-1-13
    *********************************************************************************************** '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Helper function to recursively find and remove the nth node from the end
        def removeNthHelper(node):
            # Base case: if the current node is null, return 0
            if not node:
                return 0
            # Recursive case: get the position of the next node from the end
            lastVal = removeNthHelper(node.next)

            # If the current node is the nth node from the end, remove it by adjusting pointers
            if lastVal == n:
                temp = node.next.next
                node.next = temp
            # Return the position of the current node from the end
            return lastVal + 1

        # Create a dummy node to handle edge cases and start the recursion
        dummy = ListNode()
        dummy.next = head
        removeNthHelper(dummy)
        # Return the modified list, excluding the dummy node
        return dummy.next
        