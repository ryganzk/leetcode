''' ***********************************************************************************************
    * Title: 155. Min Stack
    * Difficulty: Medium
    * Description: Design a stack that supports push, pop, top, and retrieving the minimum element
    * in constant time.
    * Source: https://leetcode.com/problems/min-stack/
    *
    * Verdict: A different function than most, this requires the user to have a bit of knowledge
    * when it comes to creating data types. An easier medium problem that is significantly more
    * interesting to complete because of this.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-14
    *********************************************************************************************** '''

class MinStack:

    # Initialization function: Initializes a stack that stores all values added to the stack, and a
    # minimum stack that stores the current minimum value in the stack
    def __init__(self):
        self.stack = []
        self.minStack = []

    # Stack push function: Pushes a number to the stack, and pushes the smaller of the current
    # minimum value and the number to the minimum stack. If there's no number currently in the
    # minimum stack, only pushes the number given
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    # Stack pop function: Pops the latest value added to the stack and minimum stack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # Stack get top function: Returns the value at the top of the stack
    def top(self) -> int:
        return self.stack[-1]     

    # Stack get min function: Returns the value at the top of the minimum stack
    def getMin(self) -> int:
        return self.minStack[-1]