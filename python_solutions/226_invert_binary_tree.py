''' ***********************************************************************************************
    * Title: 226. Invert Binary Tree
    * Difficulty: Easy
    * Description: Given the root of a binary tree, invert the tree, and return its root.
    * Source: https://leetcode.com/problems/invert-binary-tree/
    *
    * Verdict: This is the first LeetCode problem I've attempted in the past year, and to ensure I'm
    * still sharp with my problem-solving skills, I decided to solve this without using any AI tools.
    * Even though this problem is pretty straightforward, I still struggled a bit at first to visualize
    * the recursive approach needed, which confirmed to me that my skills are rusting.
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursively traverse the tree until the leaves have been reached. This practice uses DFS to
        # go as deep as possible into the tree, and once it cannot continue, it mvoes back up, swapping
        # the left and right nodes with each unwinding step
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)

            # Swap the left and right nodes
            tmp = root.left
            root.left = root.right
            root.right = tmp

        return root