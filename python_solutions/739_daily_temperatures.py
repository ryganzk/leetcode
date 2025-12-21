''' ***********************************************************************************************
    * Title: 739. Daily Temperatures
    * Difficulty: Medium
    * Description: Given an array of integers temperatures represents the daily temperatures,
    * return an array answer such that answer[i] is the number of days you have to wait after the
    * ith day to get a warmer temperature. If there is no future day for which this is possible,
    * keep answer[i] == 0 instead.
    * Source: https://leetcode.com/problems/generate-parentheses/
    *
    * Verdict: A question that confused me to begin with, as my original approach did not handle
    * adding values to the stack when a lower temperature had been received, and jsut set those
    * values to 0. A clerical error on my end, as the problem itself is fairly straightforward,
    * just make sure your knowledge on how stacks operate is solid, and focus more on adding 
    * iterators than the actualy temperature values
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-15
    *********************************************************************************************** '''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This solution requires two arrays: one that stores the temperatures iterated through in
        # a stack, and a list for the output of days gone since a higher temperature has been
        # recorded. For the output, make sure that it is as long as the input array, and that each
        # element is initialized to 0
        tempList, output = [], [0] * len(temperatures)

        # Loop over every temperature found within the input array. Make sure to use the enumerate
        # function for this, as we need to have both the element's index and temperature for the
        # steps below
        for i, t in enumerate(temperatures):
            # A while loop also needs to be declared, as we'll go down our current stack until we
            # find a temperature that is greater than the one the for loop is currently on. Make
            # sure to set a base case to make sure that the tempList contains elements
            while tempList and t > temperatures[tempList[-1]]:
                # When an temperature is reached that is colder than our current temp, we'll take
                # the index of it in the input array, pop it from the stack, and set the
                # corresponding index value in the output array equal to the current number index
                # subtracted by it. This represents the number of days that have passed before the
                # greater temperature had been found
                ind = tempList.pop()
                output[ind] = i - ind
            
            # Append the current temperature's index to the stack
            tempList.append(i)
        
        # Return the output
        return output