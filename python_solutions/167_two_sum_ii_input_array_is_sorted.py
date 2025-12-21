''' ***********************************************************************************************
    * Title: 167. Two Sum II - Input Array is Sorted
    * Difficulty: Medium
    * Description: Given a 1-indexed array of integers numbers that is already sorted in
    * non-decreasing order, find two numbers such that they add up to a specific target number. Let
    * these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <=
    * numbers.length.
    * Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    *
    * Verdict: For the sequel to the iconic two sum problem, I found this significantly easier.
    * Using pointers is much more straightforward than dictionaries or maps, and the only challenge
    * of the problem becomes writing it in O(n) compared to O(n^2)
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-13
    *********************************************************************************************** '''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # A classic problem involving two pointers, so we create one that points at the start of
        # the list, and one that points at the end (remember the last element of a list points to
        # nothing, so subtract one to get the true last element)
        lPntr, rPntr = 0, len(numbers) - 1

        # We'll loop through the steps below as long as the left and right pointers point to
        # different elements. In context of this problem, they should never point to the same
        # number, as a match would have been found by then
        while lPntr != rPntr:
            # If the target is less than the current two sum, we need to move the left pointer so
            # it points to a number greater than it is now
            if numbers[lPntr] + numbers[rPntr] < target:
                lPntr += 1
            # If the target is greater than the current two sum, we need to move the right pointer
            # so it points to a number less than it is now
            elif numbers[lPntr] + numbers[rPntr] > target:
                rPntr -= 1
            # If we reach this code block, then the current two sum equals the target number. All
            # that's left is to return the position of these pointers in a list. Keep in mind that
            # in context of this problem, the position of the pointers start at 1 rather than 0, so
            # we need to increment our current pointers to account for this change
            else:
                return [lPntr + 1, rPntr + 1]