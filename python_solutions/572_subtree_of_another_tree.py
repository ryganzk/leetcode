''' ***********************************************************************************************
    * Title: 572. Subtree of Another Tree
    * Difficulty: Easy
    * Description: Given the roots of two binary trees root and subRoot, return true if there is a
    * subtree of root with the same structure and node values of subRoot and false otherwise. A
    * subtree of a binary tree tree is a tree that consists of a node in tree and all of this
    * node's descendants. The tree tree could also be considered as a subtree of itself.
    * Source: https://leetcode.com/problems/subtree-of-another-tree/
    *
    * Verdict: I reused my isSameTree function from problem 100 to help solve this problem, making
    * this one fairly straightforward. With that being said, the time complexity of this solution is
    * O(m*n) in the worst case, as the implementation bruteforce checks every subroot node to ensure
    * it matches the roots nodes. I've seen implementations that use hashing to reduce the time
    * complexity, but it would no longer be my own work if I used that approach.
    * Language: Python
    * Time Complexity: O(m*n)
    * Space Complexity: O(m+n)
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are the same, reused from problem 100. Same Tree
        def subtreeChecker(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # If both nodes are non-null, recursively check their left and right subtrees
            if root and subRoot:
                # Recursive calls to the left and right nodes to compare their values. If either
                # subtree is not the same, return False
                if subtreeChecker(root.left, subRoot.left) == False:
                    return False
                if subtreeChecker(root.right, subRoot.right) == False:
                    return False
            # If one node is null and the other is not, the trees are not the same
            elif (not root and subRoot) or (root and not subRoot):
                return False
            # If both nodes are null, they are the same
            else:
                return True
            
            # If the values of the current nodes are not the same, return False
            if root.val != subRoot.val:
                return False
            # Getting here means the nodes are the same, so return True
            return True
        
        # Base case: if the root is null, return False
        if not root:
            return False
        # If the current nodes match, use the helper function to check if the subtrees are the same.
        # If they are, we've had a subtree match, so return True
        if root.val == subRoot.val and subtreeChecker(root, subRoot):
            return True
        # Otherwise, recursively check the left and right subtrees of the current root node. If either
        # subtree has found a match, return True to propagate that back up
        if self.isSubtree(root.left, subRoot): return True
        if self.isSubtree(root.right, subRoot): return True
        # If no matches were found, return False
        return False