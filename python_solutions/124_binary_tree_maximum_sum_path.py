''' ***********************************************************************************************
    * Title: 124. Binary Tree Maximum Path Sum
    * Difficulty: Hard
    * Description: A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
    * in the sequence has an edge connecting them. A node can only appear in the sequence at most
    * once. Note that the path does not need to pass through the root. The path sum of a path is
    * the sum of the node's values in the path. Given the root of a binary tree, return the maximum
    * path sum of any non-empty path.
    * Source: https://leetcode.com/problems/binary-tree-maximum-path-sum/
    *
    * Verdict: For a question marked as Hard, this felt pretty much on par with the Medium problems.
    * While traversal of the tree is more or less the same, the tricky part was keeping track of the
    * maximum path sum seen so far, and dealing with negative path sums by returning zero instead.
    * If other Hard binary tree problems are similar in complexity to this one, I think I'll be able
    * to handle them just fine.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-28
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum path sum to negative infinity to ensure any path sum will be higher
        maxPathSum = -math.inf

        # Helper function to traverse the tree and calculate path sums
        def sumHelper(root: Optional[TreeNode]) -> int:
            # Nonlocal modifier to access maxPathSum
            nonlocal maxPathSum
            
            # Base case: if the root is null, return 0
            if not root:
                return 0
            
            # Calculate the maximum path sum for the left and right subtrees, ignoring negative sums
            # as they would only decrease the overall path sum. Once that's taken care of, calculate
            # the current path value including the root node
            leftPath = max(sumHelper(root.left), 0)
            rightPath = max(sumHelper(root.right), 0)
            currPathVal = leftPath + root.val + rightPath

            # If the current path value is greater than the maximum path sum seen so far, update!
            if maxPathSum < currPathVal:
                maxPathSum = currPathVal

            # Return the maximum path sum including the current root and the subtree with the higher
            # path sum
            return root.val + max(leftPath, rightPath)

        # Start the recursion on the helper function, and return the max path sum when finished
        sumHelper(root)
        return maxPathSum
        