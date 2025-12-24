''' ***********************************************************************************************
    * Title: 102. Binary Tree Level Order Traversal
    * Difficulty: Medium
    * Description: Given the root of a binary tree, return the level order traversal of its nodes'
    * values. (i.e., from left to right, level by level).
    * Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
    *
    * Verdict: Just like most of the binary tree problems solved thus far, a helper function makes
    * this problem much easier to implement. I was considering using a hashmap to track the levels,
    * but figured space complexity would take a hit with converting that to a list of lists
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-24
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the list to hold the level order traversal
        orderList = []

        def orderHelper(root: Optional[TreeNode], level: int) -> None:
            # Nonlocal modifier to access orderList
            nonlocal orderList

            # Base case: if the root is null, return
            if not root:
                return
            
            # If the current level does not exist in orderList, create it
            if len(orderList) < level + 1:
                orderList.append([])
            # Append the current root's value to the appropriate level in orderList
            orderList[level].append(root.val)

            # Recurse on the left and right subtrees, increasing the level by 1
            orderHelper(root.left, level + 1)
            orderHelper(root.right, level + 1)
        
        # Start the recursion on the helper function at level 0
        orderHelper(root, 0)
        
        # Return the completed level order traversal list
        return orderList
        