''' ***********************************************************************************************
    * Title: 235. Lowest Common Ancestor of a Binary Search Tree
    * Difficulty: Medium
    * Description: Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
    * two given nodes in the BST. According to the definition of LCA on Wikipedia: “The lowest
    * common ancestor is defined between two nodes p and q as the lowest node in T that has both p
    * and q as descendants (where we allow a node to be a descendant of itself).”
    * Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    *
    * Verdict: The solution I came up with assumes an unorganized binary tree (all numbered nodes
    * are randomly organized rather than sorted from least to greatest), so even though this
    * problem can be solved in a simpler and faster way, I thought it was novel enough to showcase
    * instead of the common solution.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-23
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Create nonlocal variables to track variables needed for LCA determination
        lca = root
        lcaLayer = -1
        nodesFound = 0

        def lcaHelper(root: TreeNode, p: TreeNode, q: TreeNode, layer: int) -> bool:
            # Use nonlocal variables to track the variables outside of the helper
            nonlocal lca, lcaLayer, nodesFound
            
            # Our base case, if the root is null, return False
            if not root:
                return False

            # If the root's value matches either p or q, increment nodesFound
            if root.val == p.val or root.val == q.val:
                nodesFound += 1
                # If this is the first node found, set the lca and lcaLayer to the current root
                # and layer. This serves as our initial LCA candidate
                if nodesFound == 1:
                    lca = root
                    lcaLayer = layer

            # Recurse on the left subtree, and if it returns True, propagate that True back up
            if lcaHelper(root.left, p, q, layer + 1): return True

            # If both nodes have been found, return True to prevent further recursion
            if nodesFound == 2:
                return True

            # If the current layer is closer to the root than the previous LCA candidate, the
            # current root is now the new LCA candidate
            if lcaLayer > layer:
                lca = root
                lcaLayer = layer

            # Recurse on the right subtree, and if it returns True, propagate that True back up
            if lcaHelper(root.right, p, q, layer + 1): return True
            # Else, return False to ensure the previous node continues its search
            return False
        
        # Start the recursion on the helper function at layer 0
        lcaHelper(root, p, q, 0)

        # Once complete, return the lowest common ancestor node found
        return lca