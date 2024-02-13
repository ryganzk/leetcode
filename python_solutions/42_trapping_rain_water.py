''' ***********************************************************************************************
    * Title: 42. Trapping Rain Water
    * Difficulty: Hard
    * Description: Given n non-negative integers representing an elevation map where the width of
    * each bar is 1, compute how much water it can trap after raining.
    * Source: https://leetcode.com/problems/trapping-rain-water/
    *
    * Verdict: Not too challenging for a hard problem, but nothing to scoff at either. Serves as a
    * great test of ones knowledge of using two pointers moving towards one another. If you're
    * afraid to give the harder problems a go, this one will be a nice ramp up into the higher
    * difficulty questions
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-13
    *********************************************************************************************** '''

class Solution:
    def trap(self, height: List[int]) -> int:
        # Using two pointers would be the simplest approach to this problem. We do need to get more
        # information than these though. A varaible will be made to keep track of the number of
        # boxes filled with water throughout, as well as two integer values keeping track of the
        # shortest and longest side we've found of our current container area
        lPntr, rPntr = 0, len(height) - 1
        waterBoxes = 0
        sides = [min(height[lPntr], height[rPntr]), max(height[lPntr], height[rPntr])]

        # Keep looping as long as the left pointer is less than the right pointer
        while lPntr < rPntr:
            # Checks to see if the right pointer is less than the max side we've found so far. If
            # this is true, our tallest side is on the left, meaning we want to decrement the
            # pointer. Also, store the pointer in a temp value for calculations done later
            if height[rPntr] < sides[1]:
                rPntr -= 1
                currPntr = rPntr
            # If we reach here, it means the the right side did not satisfy the condition above,
            # meaning that the left side is smaller and thus should be incremented. Store it as a
            # temp value as well!
            else:
                lPntr += 1
                currPntr = lPntr

            # Both of these calculations are used to update the min and max sides we're storing.
            # For the smaller side, we'll take the minimum of the current left and right pointer
            # values if it's greater than the current minimum side. For the larger side, we'll take
            # the maximum of the current left and right pointer values if it's greater than the
            # current maximum side
            sides[0] = max(min(height[lPntr], height[rPntr]), sides[0])
            sides[1] = max(max(height[lPntr], height[rPntr]), sides[1])

            # Here we'll check the height difference of the minimum side with the height of the
            # current pointer. If the value is above zero, that means we've found a space that can
            # contain water. All we need to do is add that space to the output variable we declared
            # at the beginning
            heightDiff = sides[0] - height[currPntr]
            if heightDiff > 0:
                waterBoxes += heightDiff

        # Computation has finished, return the result
        return waterBoxes  