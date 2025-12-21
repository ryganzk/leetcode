''' ***********************************************************************************************
    * Title: 206. Reverse Linked List
    * Difficulty: Easy
    * Description: Given the head of a singly linked list, reverse the list, and return the reversed
    * list.
    * Source: https://leetcode.com/problems/reverse-linked-list/
    *
    * Verdict: A practical problem with reversing a linked list, it's nothing special but important
    * to know as linked lists are a solid data structure that finds implementations in a lot of
    * software architectures. My approach was to use recursion to reverse the list node by node, but
    * I'm certain there are quite a few alternative approaches to this problem out there.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-9-08
    *********************************************************************************************** '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or only has one element, return it as it is
        if not head or not head.next:
            return head

        # The main recursive function, takes in the previous node as well as the current node to allow
        # for reversing the list structure
        def reverseNode(prevNode: Optional[ListNode], currNode: Optional[ListNode]) -> Optional[ListNode]:
            # If the current node is not pointing to another node, it is the last element in the list,
            # so this node will point to the previous node and be returned
            if not currNode.next:
                currNode.next = prevNode
                return currNode

            # Call another level of recursion on the current node and it's child node
            newHead = reverseNode(currNode, currNode.next)
            # Set the current node's next node to the previous node, and return the new head returned by
            # the last step
            currNode.next = prevNode
            return newHead

        # The entry point for recursion, returns a reversed list while passing in a None for the previous
        # element (we do not want our last element pointing to something else) as well as the current head
        return reverseNode(None, head)
