''' ***********************************************************************************************
    * Title: 230. Kth Smallest Element in a BST
    * Difficulty: Medium
    * Description: Given the root of a binary search tree, and an integer k, return the kth smallest
    * value (1-indexed) of all the values of the nodes in the tree.
    * Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    *
    * Verdict: Unlike a previous problem in which I solved for a tree that may or may not be balanced,
    * this solution assumes that the tree is balanced to begin with, which was enough for Leetcode to
    * accept. While I hit a few snags when coding up this solution due to how Python treats
    * true/false operations with integers, I was able to get through this problem fairly quickly.
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
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Defines a counter to track how many nodes have been processed so far
        nodesCounted = 0

        def kthSmallestHelper(root: Optional[TreeNode], k: int) -> int:
            # Nonlocal modifier to access nodesCounted
            nonlocal nodesCounted

            # Base case: if the root is null, return None
            if not root:
                return None
            
            # Recurse on the left subtree. If the result of the left subtree is not None, return it.
            # This indicates that the kth smallest element has been found in the left subtree. The
            # comparison also checks for 0, as that is a valid node value that could be returned
            # (Python treats 0 as False in boolean contexts)
            leftResult = kthSmallestHelper(root.left, k)
            if leftResult or leftResult == 0: return leftResult

            # After processing the left subtree, check if the current node is the kth smallest node.
            # If it is, return its value. If not, increment the nodesCounted counter
            if nodesCounted == k - 1:
                return root.val
            else:
                nodesCounted += 1

            # Recurse on the right subtree. If the result of the right subtree is not None, return it.
            rightResult = kthSmallestHelper(root.right, k)
            if rightResult or rightResult == 0: return rightResult
        
        # Start the recursion on the helper function and return its result
        return kthSmallestHelper(root, k)
