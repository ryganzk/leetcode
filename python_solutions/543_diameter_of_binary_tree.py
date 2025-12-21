''' ***********************************************************************************************
    * Title: 543. Diameter of Binary Tree
    * Difficulty: Easy
    * Description: Given the root of a binary tree, return the length of the diameter of the tree.
    * The diameter of a binary tree is the length of the longest path between any two nodes in a
    * tree. This path may or may not pass through the root. The length of a path between two nodes
    * is represented by the number of edges between them.
    * Source: https://leetcode.com/problems/diameter-of-binary-tree/
    *
    * Verdict: I read the comments for this problem on LeetCode, and noticed many people were
    * complaining that the difficulty of the problem should be Medium at least. I'm inclined to agree,
    * although in my case, this is because calling the longest path of the tree its "diameter" seemed
    * intentionally confusing. This problem also helped remind me that local and nonlocal calls exist,
    * as I was wondering why my result variable wasn't being read in my helper function.
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        # The recursive helper function to calculate the diameter of the tree
        def diameterHelper(root: Optional[TreeNode]) -> int:
            # Ensures result can update outside of this loop
            nonlocal result

            # Return 0, as we've hit the bottom of a path
            if not root:
                return 0

            # Recusrive calls to the left and right nodes to calculate their heights
            leftHeight = diameterHelper(root.left)
            rightHeight = diameterHelper(root.right)
            # Updates the result if the sum of the left and right heights is greater than it is currently
            result = max(result, leftHeight + rightHeight)
            
            # Return the sum of the largest path thus far, plus 1 to account for the current node
            return 1 + max(leftHeight, rightHeight)

        diameterHelper(root)
        return result