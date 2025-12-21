''' ***********************************************************************************************
    * Title: 100. Same Tree
    * Difficulty: Easy
    * Description: Given the roots of two binary trees p and q, write a function to check if they
    * are the same or not. Two binary trees are considered the same if they are structurally
    * identical, and the nodes have the same value.
    * Source: https://leetcode.com/problems/same-tree/
    *
    * Verdict: Not too complicated of a problem overall. I originally did my node comparisons with
    * the current node's leaves, but due to this not working for single-node trees, I realized I
    * could go even simpler by just comparing the current nodes to each other. Yet again, I
    * overcomplicate the amount of work needed.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-21
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are non-null, recursively check their left and right subtrees
        if p and q:
            # Recursive calls to the left and right nodes to compare their values. If either
            # subtree is not the same, return False
            if self.isSameTree(p.left, q.left) == False:
                return False
            if self.isSameTree(p.right, q.right) == False:
                return False
        # If one node is null and the other is not, the trees are not the same
        elif (not p and q) or (p and not q):
            return False
        # If both nodes are null, they are the same
        else:
            return True
        
        # If the values of the current nodes are not the same, return False
        if p.val != q.val:
            return False
        # Getting here means the nodes are the same, so return True
        return True