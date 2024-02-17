''' ***********************************************************************************************
    * Title: 84. Largest Rectangle in Histogram
    * Difficulty: Medium
    * Description: Return the number of car fleets that will arrive at the destination.
    * Source: https://leetcode.com/problems/car-fleet/
    *
    * Verdict: Definitely the hardest problem I've solved until this point (have only solved 20+
    * at the moment). Similar in structure to 42. Trapping Rain Water, except iteration is made
    * much harder as there are many examples where small rectangles could net the greatest area.
    * I'll admit this wasn't a problem that I was able to solve without some guidance, so try at
    * your own risk
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-17
    *********************************************************************************************** '''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append a 0 to the end of the height array to signify the end of the given amount of
        # rectangles
        heights.append(0)
        # Initialize a stack of indices, and add one pointing to the very end of the stack (used
        # for entry in the coming for loop). Also initialize an output variable storing the max
        # area found
        stack = [-1]
        maxArea = 0
        
        # Loop over the index/height pairs in the heights array (made easy through using the
        # enumerate function given to use by Python)
        for i, h in enumerate(heights):
            # Loop the below function while the current height is less than the height given by the
            # last index in the stack
            while h < heights[stack[-1]]:
                # Calculate the current max area, using the product of the height provided by the
                # current index on the stack with the distance from the popped index from the one
                # we're currently iterating on
                maxArea = max(maxArea, heights[stack.pop()] * (i - stack[-1] - 1))
            # Append the current index on the stack for future use
            stack.append(i)
        
        # Return the max area
        return maxArea