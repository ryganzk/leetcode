''' ***********************************************************************************************
    * Title: 1448. Count Good Nodes in Binary Tree
    * Difficulty: Medium
    * Description: Given a binary tree root, a node X in the tree is named good if in the path from
    * root to X there are no nodes with a value greater than X. Return the number of good nodes in
    * the binary tree.
    * Source: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
    *
    * Verdict: These binary tree problems are getting so much easier to solve, I finished this one
    * in under five minutes. The hardest part of this question was figuring out what would count as
    * a good node and how to track which ones are and aren't, which in my instance, was easily done
    * through a counter and keeping track of the maximum node value seen on the path from the root to
    * the current node.
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
    def goodNodes(self, root: TreeNode) -> int:
        # Initialize counter for good nodes
        goodNodeCount = 0

        # Helper function to traverse the tree and count good nodes. Math.inf is used as the initial
        # maxNode value to ensure the root node is always considered a good node (remember the nodes
        # can be negative values)
        def goodNodeHelper(root: TreeNode, maxNode: int=-math.inf) -> None:
            # Nonlocal modifier to access goodNodeCount
            nonlocal goodNodeCount

            # Base case: if the root is null, return
            if not root:
                return
            
            # If the current node's value is greater than or equal to the maxNode seen so far,
            # increment the counter and update maxNode to the current node's value
            if root.val >= maxNode:
                goodNodeCount += 1
                maxNode = root.val
            
            # Recurse on the left and right subtrees, passing the updated maxNode value
            goodNodeHelper(root.left, maxNode)
            goodNodeHelper(root.right, maxNode)
            
        # Start the recursion on the helper function and return the good node count when finished
        goodNodeHelper(root)
        return goodNodeCount