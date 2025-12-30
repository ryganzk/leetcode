''' ***********************************************************************************************
    * Title: 297. Serialize and Deserialize Binary Tree
    * Difficulty: Hard
    * Description: Serialization is the process of converting a data structure or object into a
    * sequence of bits so that it can be stored in a file or memory buffer, or transmitted across
    * a network connection link to be reconstructed later in the same or another computer
    * environment. Design an algorithm to serialize and deserialize a binary tree. There is no
    * restriction on how your serialization/deserialization algorithm should work. You just need to
    * ensure that a binary tree can be serialized to a string and this string can be deserialized
    * to the original tree structure.
    * Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
    *
    * Verdict: This one was a time sink. Originally I had misinterpreted the structure of the
    * binary tree, as I assumed that every single node, including null nodes, needed to be
    * represented in the serialized string, which turns out isn't the case, as those nodes will be
    * skipped over. Therefore, I have two solutions for this problem: this one being the intended
    * solution, and the other being my solution assuming every null node needed to be represented.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-30
    *********************************************************************************************** '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Empty list to hold node values during traversal
        nodeList = []
        # Helper function to perform pre-order traversal and build the serialized string
        def serializeHelper(root):
            # Base case: if the root is null, append 'null' to the list and return
            if not root:
                nodeList.append('null')
                return

            # Append the current node's value and recurse on left and right subtrees
            nodeList.append(str(root.val))
            serializeHelper(root.left)
            serializeHelper(root.right)

        # Start the recursion on the helper function
        serializeHelper(root)
        # Join the list into a comma-separated string and return
        return ",".join(nodeList)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Split the serialized string into a list and initialize position pointer, stripping
        # spaces just in case
        nodeList = [s.strip() for s in data.split(',')]
        pos = 0

        # Helper function to reconstruct the tree from the node list
        def deserializeHelper():
            # Nonlocal modifier to access the position pointer
            nonlocal pos

            # Base case: if the current node is 'null', increment position and return None
            if nodeList[pos] == 'null':
                pos += 1
                return None
            
            # Create the current node, increment position, and recurse on left and right subtrees
            node = TreeNode(nodeList[pos])
            pos += 1
            node.left = deserializeHelper()
            node.right = deserializeHelper()
            # Once finished, return the node
            return node

        # Start the recursion on the helper function and return the reconstructed tree
        return deserializeHelper()
