''' ***********************************************************************************************
    * Title: 199. Binary Tree Right Side View
    * Difficulty: Medium
    * Description: Given the root of a binary tree, imagine yourself standing on the right side of
    * it, return the values of the nodes you can see ordered from top to bottom.
    * Source: https://leetcode.com/problems/binary-tree-right-side-view/
    *
    * Verdict: This solution combines my previous logic of handling level-order traversal while
    * keeping track of the current level the loop is on with a dictionary to store the rightmost node
    * at each level. A fun problem that feels on the easier side of medium difficulty, or maybe I'm
    * that much better at solving binary tree problems now.
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Dictionary to hold the rightmost node at each level
        rightmostNodesDict = {}

        # Helper function to perform a modified pre-order traversal
        def rightSideHelper(root: Optional[TreeNode], level: int = 0) -> None:
            # Nonlocal modifier to access rightmostNodesDict
            nonlocal rightmostNodesDict

            # Base case: if the root is null, return
            if not root:
                return

            # If the current level is not in the dictionary, store the level and node value as a
            # dictionary key-value pair
            if level not in rightmostNodesDict:
                rightmostNodesDict[level] = root.val

            # Recurse on the right subtree first to ensure rightmost nodes are processed first, then
            # the left subtree to ensure full tree coverage
            rightSideHelper(root.right, level + 1)
            rightSideHelper(root.left, level + 1)
        
        # Start the recursion on the helper function at level 0 (set in the helper's default arg)
        rightSideHelper(root)

        # Convert the dictionary values to a list and return it
        return [value for value in rightmostNodesDict.values()]