''' ***********************************************************************************************
    * Title: 104. Maximum Depth of Binary Tree
    * Difficulty: Easy
    * Description: Given the root of a binary tree, return its maximum depth. A binary tree's
    * maximum depth is the number of nodes along the longest path from the root node down to the
    * farthest leaf node.
    * Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    *
    * Verdict: A bit trickier of a problem compared to 226. Invert Binary Tree, as even though
    * recursion is still used, you're required to keep track of the maximum depth at each node. My
    * original approach to this problem was to set a current and maximum depth varaible in the main
    * function, and deal with the recursion in a helper function, but after stepping back I remembered
    * that returning 0 at a leaf node and adding 1 for each recursive step back up the tree would make
    * for a simpler and cleaner solution.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-20
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the current node is not null, recursively call maxDepth on the left and right nodes,
        # add 1 to each to account for the current node, and return the maximum of the both depths
        if root:
            maxLeft = self.maxDepth(root.left) + 1
            maxRight = self.maxDepth(root.right) + 1
            return max(maxLeft, maxRight)
        # The bottom of the tree has been reached, so return 0
        else:
            return 0