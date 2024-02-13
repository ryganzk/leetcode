''' ***********************************************************************************************
    * Title: 11. Container With Most Water
    * Difficulty: Medium
    * Description: You are given an integer array height of length n. There are n vertical lines
    * drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    * Source: https://leetcode.com/problems/container-with-most-water/
    *
    * Verdict: Even for a medium level problem, I felt the problem to be pretty simple in nature.
    * The most grueling part is figuring out the proper way to calculate the container size based
    * on the two pointers used, but beyond that this problem is easy enough
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-13
    *********************************************************************************************** '''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # A two pointer problem if I've ever seen one! Create a max container for the output
        # integer, and a left and right pointer for the iteration steps below
        maxContainer = 0
        lPntr, rPntr = 0, len(height) - 1

        # Continue the loop while the left pointer is less than the right pointer
        while lPntr < rPntr:
            # The calculation for the container size will require a bit of an explanation. First
            # the smaller of the heights is taken, as the max size that will not cause any leakage
            # needs to be determined. Now that the true height has been found, all we need to do is
            # multiply it by the length, which is the right pointer subtracted by the left pointer,
            # to get the full area of the container
            containerSize = min(height[lPntr], height[rPntr]) * (rPntr - lPntr)
            # If the current container is greater than the current max, set the max to be the
            # current container
            maxContainer = max(containerSize, maxContainer)

            # Since we want to keep the height of the tallest side we've found so far, check if the
            # height referenced by the right pointer is greater than the height referenced by the
            # left pointer. If it is, increment the left pointer. If not, increment the right
            #pointer
            if height[rPntr] > height[lPntr]:
                lPntr += 1
            else:
                rPntr -= 1

        # At this point, the max container has been found, so return it to solve the problem
        return maxContainer