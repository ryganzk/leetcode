''' ***********************************************************************************************
    * Title: 110. Balanced Binary Tree
    * Difficulty: Easy
    * Description: Given a binary tree, determine if it is height-balanced.
    * Source: https://leetcode.com/problems/balanced-binary-tree/
    *
    * Verdict: While I might've used some assistance with the other problems that I've solved today
    * involving binary trees, I can safely say that the solution shown is 100% my own work, and it
    * shows since I used integer math quite a bit to flag an unbalanced tree once it's been detected.
    * I had a bit of fun with this one, and I can finally feel my neurons firing once again ;).
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive helper function to determine if the tree is balanced
        def balancedHelper(root: Optional[TreeNode]) -> int:
            # Returns a zero if the bottom of a path is reached
            if not root:
                return 0
            
            # Recursive calls to the left and right nodes to calculate their heights
            leftHeight = balancedHelper(root.left) + 1
            rightHeight = balancedHelper(root.right) + 1

            # If either subtree is unbalanced (which is indicated if either height is -1, as that is
            # not a possible height for a path), or the current node is unbalanced, return -2 as our
            # flag. -2 is chosen because when the step unwinds, the height will be incremented by 1, so
            # this value ensures that the height can no longer become positive again
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -2
            
            # If the tree is currently balanced, return the maximum height of the two subtrees
            return max(leftHeight, rightHeight)

        # A balanced tree will never return a negative height, so if a negative is returned, the tree
        # is unbalanced
        return balancedHelper(root) > -1