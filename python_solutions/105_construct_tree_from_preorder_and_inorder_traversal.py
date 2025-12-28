''' ***********************************************************************************************
    * Title: 105. Construct Binary Tree from Preorder and Inorder Traversal
    * Difficulty: Medium
    * Description: Given two integer arrays preorder and inorder where preorder is the preorder
    * traversal of a binary tree and inorder is the inorder traversal of the same tree, construct
    * and return the binary tree.
    * Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    *
    * Verdict: While most of the previous binary tree problems had a similar structure of finding
    * a particular node or nodes in a pre-exisiting tree that fulfill certain requirements, this
    * problem required building a tree from scratch. This felt much harder than the others as a
    * result, so I'm curious to see what a Hard difficulty binary tree problem will look like.
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
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Dictionary to hold the inorder values and their corresponding indices for O(1) lookup, as
        # well as a current index pointer for preorder traversal
        orderDict = {item: index for index, item in enumerate(inorder)}
        currIdx = 0

        def buildTreeHelper(leftIdx: int, rightIdx: int) -> Optional[TreeNode]:
            # Nonlocal modifier to access currIdx
            nonlocal currIdx

            # Base case: if the left index exceeds the right index, return None
            if leftIdx > rightIdx:
                return
            
            # Create the root node using the current index in preorder
            rootVal = preorder[currIdx]
            root = TreeNode(rootVal)

            # Increment currIdx to point to the next node in preorder, and use the inorder
            # dictionary to find the midpoint for left and right subtree construction
            currIdx += 1
            midpoint = orderDict[rootVal]

            # Using the midpoint, recursively build the left and right subtrees
            root.left = buildTreeHelper(leftIdx, midpoint - 1)
            root.right = buildTreeHelper(midpoint + 1, rightIdx)
            return root

        # Start the recursion on the helper function with the full range of inorder indices
        return buildTreeHelper(0, len(orderDict) - 1)
