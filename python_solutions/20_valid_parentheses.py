''' ***********************************************************************************************
    * Title: 20. Valid Parentheses
    * Difficulty: Easy
    * Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    * determine if the input string is valid.
    * Source: https://leetcode.com/problems/valid-parentheses/
    *
    * Verdict: A nice introduction into how to effectively utilize stacks. I consider the hardest
    * part of this lab to be condensing the logic, rather than actually mapping the problem out.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-14
    *********************************************************************************************** '''

class Solution:
    def isValid(self, s: str) -> bool:
        # This problem requires the use of a stack, so we'll create a list to emulate one
        charStack = []

        # Iterate over every parenthesis found in the string
        for x in s:
            # If we find a valid left parenthesis, append it to the stack
            if x == "(" or x == "{" or x == "[":
                charStack.append(x)
            # If we get here, we're going to need to remove a parenthesis from the stack. If
            # there's nothing on the stack that we can remove, return False, as the string is not
            # valid
            elif len(charStack) == 0:
                return False
            # If the current parenthesis is a ), pop the last character from the stack. If these
            # parentheses do not match, then return False
            elif x == ")" and charStack.pop() != "(":
                return False
            # If the current parenthesis is a }, pop the last character from the stack. If these
            # parentheses do not match, then return False
            elif x == "}" and charStack.pop() != "{":
                return False
            # If the current parenthesis is a ], pop the last character from the stack. If these
            # parentheses do not match, then return False
            elif x == "]" and charStack.pop() != "[":
                return False
        
        # Every parenthesis in the string has been iterated over. If there are any left in the
        # stack, return False, as we have some parentheses left over that do not contain a match
        if len(charStack) > 0:
            return False

        # At this point, the stack is completely empty, meaning that all parentheses have matched
        # up! Return True!
        return True