''' ***********************************************************************************************
    * Title: 98. Validate Binary Search Tree
    * Difficulty: Medium
    * Description: Given the root of a binary tree, determine if it is a valid binary search tree
    * (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with
    * keys strictly less than the node's key. The right subtree of a node contains only nodes with
    * keys strictly greater than the node's key. Both the left and right subtrees must also be
    * binary search trees.
    * Source: https://leetcode.com/problems/validate-binary-search-tree/
    *
    * Verdict: I'm glad I figured out the use cases of nonlocal variables in a previous problem, as
    * they make this implementation much cleaner than passing variables through the recursive
    * function calls. A fairly straightforward problem, the only challenge here is ensuring the
    * proper values are compared and at which point in the recursion that should occur.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-26
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initialize the highest value to negative infinity, as the first value read should always be
        # higher than it
        highestVal = -math.inf

        def validBSTHelper(root: Optional[TreeNode]):
            # Nonlocal modifier to access highestVal
            nonlocal highestVal

            # Base case: if the root is null, return True
            if not root:
                return True
            
            # If the left subtree is invalid, the whole tree will be invalid, so return False
            if not validBSTHelper(root.left): return False

            # If the current node's value is greater than the highest value seen so far, update
            # highestVal to the current node's value. Else, the BST property is violated, so return
            # False
            if root.val > highestVal:
                highestVal = root.val
            else:
                return False

            # If the right subtree is invalid, the whole tree will be invalid, so return False. Else,
            # the subtree at this point is valid, so return True
            if not validBSTHelper(root.right): return False
            return True
        
        # Start the recursion on the helper function and return its result
        return validBSTHelper(root)