''' ***********************************************************************************************
    * Title: 217. Contains Duplicates
    * Difficulty: Easy
    * Description: Given an integer array nums, return true if any value appears at least twice in
    * the array, and return false if every element is distinct.
    * Source: https://leetcode.com/problems/contains-duplicate/
    *
    * Verdict: An extremly simple problem that serves as a great introduction to sets. It's very
    * possible to sort the array and step through to make sure no repeats exist, but sets reduce
    * runtime considerable
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Based on the problem description, using a set would yield the quickest solution
        dupSet = set()

        # Add every number in the array to the list. Because sets by definition cannot contain
        # duplicate values, each number in the set will be unique
        for n in nums:
            dupSet.add(n)

        # Lastly, compare the length of the set with the input array. If they match, no duplicates
        # were found, which returns False
        if len(nums) == len(dupSet):
            return False
        
        # If the code reaches this point, then the lengths above did not match, meaning the input
        # array did in fact contain duplicate values. In this case, return True
        return True