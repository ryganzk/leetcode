''' ***********************************************************************************************
    * Title: 150. Evaluate Reverse Polish Notation
    * Difficulty: Medium
    * Description: You are given an array of strings tokens that represents an arithmetic
    * expression in a Reverse Polish Notation. Evaluate the expression. Return an integer that
    * represents the value of the expression.
    * Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
    *
    * Verdict: A simpler medium level problem requiring knowledge of how a stack functions. The two
    * areas I recommend lookig out for is handling postive AND negative tokens, as well as
    * maintaining a correct order when handling certain operations
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-15
    *********************************************************************************************** '''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # This problem will utilize a stack. Creating a list will service us just fine
        stack = []

        # Iterate over every character found within the token list
        for c in tokens:
            # This if statement checks to see if the current token is a number. If so, it'll add it
            # to the stack. Keep in mind that an additional check will need to be performed to
            # handle negative numbers, as they are not considered to be numeric values
            if c.isnumeric() or (c[0] == '-' and c[1:].isnumeric()):
                stack.append(int(c))
            # If the token found is a +, we'll pop off the last two numbers from the stack, add
            # them together, and append the result back to the stack
            elif c == '+':
                stack.append(stack.pop() + stack.pop())
            # If the token found is a -, we'll pop off the first number from the stack and store it
            # as a temp value, and then subtract it from the next pop to the stack, where it'll be
            # appended back to the stack. Remember with subtraction, the ordering of the variables
            # will change the result!
            elif c == '-':
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            # If the token found is a *, we'll pop off the last two numbers from the stack,
            # multiply them together, and append the result back to the stack. Ordering does not
            # matter with multiplication
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            # If the token found is a -, we'll pop off the first number from the stack and store it
            # as a temp value, and then divide it from the next pop to the stack, where it'll be
            # appended back to the stack. As with subtraction, make sure to order the variables
            # correctly
            elif c == '/':
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
        
        # By this point, there should be one more integer remaining on the stack, which will be our
        # result! All that remains is to return the number
        return stack[0]