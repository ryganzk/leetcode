''' ***********************************************************************************************
    * Title: 238. Product of Array Except Self
    * Difficulty: Medium
    * Description: Given an integer array nums, return an array answer such that answer[i] is equal
    * to the product of all the elements of nums except nums[i].
    * Source: https://leetcode.com/problems/product-of-array-except-self/
    *
    * Verdict: An interesting problem that requires two-way array traversal to accomplish. This one
    * requires a resonable plan of action going in, and hand-drawing the writing and iterating
    * process will help immensly in understanding the structure of the answer
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Before working on this problem, we need to create an output array, a prefix integer, and
        # a postfix integer. The output array matches the same length as the input array, since
        # it will be filled with the solution numbers. It's also important that every value is set
        # to one, as we'll be using multiplication to change these values, which won't work out
        # nicely with the default 0s an array generates! The prefix and postfix are used for the
        # loops below, just make sure that the prefix is set to the first element of the input
        # array, and the postfix is set to the last element of the input array
        out = [1] * len(nums)
        prefix = nums[0]
        postfix = nums[len(nums) - 1]

        # Starting at the second number in the output array, multiply the number by the prefix, and
        # increment that prefix to the matching number in the input array. Repeat this step until
        # the end of the output array has been reached
        for i in range(1, len(out)):
            out[i] *= prefix
            prefix *= nums[i]

        # Now reverse what we did in the loop above, starting at the second to last element in the
        # output array, and working down the list until the first element has been reached, all the
        # while multiplying the current number in the output array by the postfix, and multiplying
        # the postfix to the corresponding number in the input array
        for i in range(len(out) - 2, -1, -1):
            out[i] *= postfix
            postfix *= nums[i]

        # Once our output array has been completely filled and updated, return the result
        return out