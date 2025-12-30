''' ***********************************************************************************************
    * Title: 297. Serialize and Deserialize Binary Tree [Invalid Solution]
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
    * Verdict: My original and unoptimal solution to this problem, which assumed that every null
    * node needed to be represented in the serialized string. The approach uses a heap to store node
    * positions (used through an algorithm tying the node's position compared to others in the
    * level) before combining into a serialized stringThis solution works, but uses up a hefty
    * amount of memory for large and unbalanced trees. I kept this solution to show my initial work
    * before simplifying it.
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
        # Initialize list and dictionary to hold node values and their positions
        nodeList, nodeDict = [], {}
        # Helper function to perform pre-order traversal and build the node dictionary
        def serializeHelper(root, level: int=0, pos: int=0):
            # Nonlocal modifier to access nodeDict
            nonlocal nodeDict

            # Base case: if the root is null, return
            if not root:
                return

            # Store the node's value in the dictionary using its calculated position. This is equal
            # to (2^level) + pos, where level is the current tree level (root being level 0) and
            # pos is the position within that level (leftmost node being position 0)
            nodeDict[(2 ** level) + pos] = root.val
            
            # Recurse on the left and right subtrees, updating level and position accordingly. Both
            # child's level will be once greater than the current one. The next left child's position
            # is (2 * pos) and the next right child's position is (2 * pos) + 1
            serializeHelper(root.left, level + 1, (2 * pos))
            serializeHelper(root.right, level + 1, (2 * pos) + 1)

        # Start the recursion on the helper function
        serializeHelper(root)

        # Build the serialized string by iterating through the node dictionary in order of
        # positions, appending "null" for any missing nodes
        i = 1
        while nodeDict:
            value = nodeDict.pop(i, None)
            nodeList.append(str(value) if value is not None else "null")
            i += 1

        # Join the list into a comma-separated string and return
        return ",".join(nodeList)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Split the serialized string into a list, stripping spaces just in case
        nodeList = [s.strip() for s in data.split(',')]
        # Handle edge case of empty tree, which will have an empty first element due to
        # how the serialization function above works
        if nodeList[0] == '': return None

        # Helper function to reconstruct the tree from the node list
        def deserializeHelper(level: int=0, pos: int=0):
            # Calculate the tree's value based on the current level and position. Essentially, the
            # tree value is equal to (2^level) + pos, subtracted by 1 to account for zero-based
            # indexing in the nodeList
            treeVal = (2 ** level) + pos - 1
            # Base case: if the calculated tree value is out of bounds or the node is 'null', return
            if treeVal >= len(nodeList) or nodeList[treeVal] == 'null':
                return

            # Create the current node (remember the cast to int), print it for debugging, and recurse
            # on the left and right subtrees, updating level and position accordingly. The values for
            # the child's level and position are the same as in the serializeHelper function
            root = TreeNode(int(nodeList[treeVal]))
            root.left = deserializeHelper(level + 1, (2 * pos))
            root.right = deserializeHelper(level + 1, (2 * pos) + 1)
            # Once finished, return the node
            return root

        # Start the recursion on the helper function and return the reconstructed tree
        return deserializeHelper()
        