''' ***********************************************************************************************
    * Title: 153. Find Minimum In Rotated Sorted Array
    * Difficulty: Medium
    * Description: Given the sorted rotated array nums of unique elements, return the minimum
    * element of this array. You must write an algorithm that runs in O(log n) time.
    * Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    *
    * Verdict: A problem that legitemately took me three minutes to solve, and what I consider to
    * be a companion to 704. Binary Search, except somehow easier. I'm baffled how this is
    * considered a medium level problem, as it not only can be solved in more-or-less the same way
    * as the question mentioned above, but easier due to not needing any base cases or exceptions
    * being caught. Forgive me if my explanation is not as detailed as usual, I feel as I'm just
    * repeating myself if I delve more into this problem
    * Language: Python
    * Time Complexity: O(logn)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-19
    *********************************************************************************************** '''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Create a left and right iterator, setting the left to 0, and the right to the length of
        # the input array subtracted by 1. Also create an output variable that stores the smallest
        # number, setting it to the first element at the moment
        l, r = 0, len(nums) - 1
        out = nums[0]

        # Repeat until the left iterator is no longer less than or equal to the right iterator
        while l <= r:
            # Find the midpoint from the range between the left and right iterators
            mid = (l + r) // 2

            # If the number pointed to by the current midpoint is less than the current minimum
            # value found, set that output varaible equal to this number, and set the right
            # iterator to point to the variable to the left of the current number
            if nums[mid] < out:
                out = nums[mid]
                r = mid - 1
            # If not, increase the left iterator to point to the variable past the current midpoint
            else:
                l = mid + 1

        # Return the result
        return out