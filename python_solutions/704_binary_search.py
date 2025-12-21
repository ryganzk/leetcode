''' ***********************************************************************************************
    * Title: 704. Binary Search
    * Difficulty: Easy
    * Description: Given an array of integers nums which is sorted in ascending order, and an
    * integer target, write a function to search target in nums. If target exists, then return its
    * index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.
    * Source: https://leetcode.com/problems/binary-search/
    *
    * Verdict: I remember writing a binary search function in my sophomore year in college, which
    * took me over two hours to write out. This is pretty much the exact same lab, which took me
    * twenty minutes today. Working out the iterator position after each array check was the most
    * difficult part, as it took me a few attemtps to get it working properly. Definitely draw a
    * sketch of each access if it helps
    * Language: Python
    * Time Complexity: O(logn)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-17
    *********************************************************************************************** '''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Create two iterators, one at the leftmsot element in the array, and one at the rightmost
        l, r = 0, len(nums) - 1

        # A base case that returns the first position if there's only one number in the array, and
        # if it also matches the target value
        if len(nums) == 1 and nums[0] == target:
            return 0

        # Repeat the code below as long as the left iterator is less than the right iterator
        while l <= r:
            # Calculates the middle element of the two iterators we have. This way, we'll be able
            # to considerably reduce the search range in the steps below
            mid = (l + r) // 2

            # If the number pointed to by the middle iterator is lower than the target, move the
            # left iterator to the next element. This is done as in a sorted array, none of the
            # elements before the new left iterator can be equal to the target
            if nums[mid] < target:
                l = mid + 1
            # If the number pointed to by the middle iterator is greater than the target, move the
            # right iterator to the previous element. Like above, none of the elements before the
            # new rightt iterator can be equal to the target
            elif nums[mid] > target:
                r = mid - 1
            # If none of the above two statements have been called, the number pointed to by the
            # middle iterator must be equal to the target. In this case, return that iterator
            else:
                return mid

        # The array does not contain a number matching the target. Return -1 to signify a matching
        # iterator does not exist
        return -1