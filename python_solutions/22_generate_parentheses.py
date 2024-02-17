''' ***********************************************************************************************
    * Title: 22. Generate Parentheses
    * Difficulty: Medium
    * Description: Given n pairs of parentheses, write a function to generate all combinations of
    * well-formed parentheses.
    * Source: https://leetcode.com/problems/generate-parentheses/
    *
    * Verdict: A step up from 20. Valid Parentheses, now needing the use of a stack AND a recursive
    * function to complete. Due to the nature of recursive functions, I found creating the internal
    * logic of the code to be a bit frustrating at times. Unfortunately, I don't believe there's a
    * way to improve the time complexity, as while our n increases, the number of possible
    * solutions will exponentially increase
    * Time Complexity: O(2^n)
    * Space Complexity: O(2^n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-15
    *********************************************************************************************** '''

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # This problem utilizes an array for output, and a string for storing the current string
        # holding the current parentheses
        output = []
        parenStr = ""

        # The easiest solution I managed to devise uses a recursive function to control code flow.
        # Our function takes in the number of left and right parentheses currently used
        def backtrack(leftP, rightP):
            # We need to define our parenthesis string as nonlocal to be able to use it in context
            # of the function
            nonlocal parenStr

            # If we've created a valid parentheses string, meaning that the number of left and
            # right parentheses used match the number of maximum parentheses able to be used, then
            # append it to the output array, and back out of the current function call
            if leftP == rightP == n:
                output.append(parenStr)
                return
            
            # If a valid parentheses string hasn't been made yet, and the number of left
            # parentheses used is less than the maximum amount of left parentheses used, one will
            # be added to the parentheses string, and another call to our funciton is made, with
            # the left parentheses argument incremented. Once this function completes, this left
            # parenthesis will be removed from the string
            if leftP < n:
                parenStr = parenStr + "("
                backtrack(leftP + 1, rightP)
                parenStr = parenStr[:-1]
            
            # Likewise, if a valid parentheses string hasn't been made yet, and the number of right
            # parentheses used is less than the maximum amount of right parentheses used, one will
            # be added to the parentheses string, and another call to our funciton is made, with
            # the right parentheses argument incremented. Once this function completes, this right
            # parenthesis will be removed from the string
            if rightP < leftP:
                parenStr = parenStr + ")"
                backtrack(leftP, rightP + 1)
                parenStr = parenStr[:-1]

        # Call to the recursive function with nothing added to the parentheses string. By the time
        # we exit the function, our output array will be fully populated with the results
        backtrack(0, 0)

        # Return the output
        return output  