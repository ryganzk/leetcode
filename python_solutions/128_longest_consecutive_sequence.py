''' ***********************************************************************************************
    * Title: 128. Longest Consecutive Sequence
    * Difficulty: Medium
    * Description: Given an unsorted array of integers nums, return the length of the longest
    * consecutive elements sequence.
    * Source: https://leetcode.com/problems/longest-consecutive-sequence/
    *
    * Verdict: I found this problem to be a fairly straightforward usage of sets. While it didn't
    * do anything I personally found interesting, it's a good problem for those trying to brush up
    * on sets, and show off a case where using sets is a smarter option than a map or dict
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # My approach to this problem was to convert the input array into a set, easing up the
        # computation time with searching for consecutive numbers. I also created an output
        # variable, and set it to zero because a sequence has not been found as of yet
        numSet = set(nums)
        out = 0

        # Iterates through every number in the number set we created above
        for n in numSet:
            # This line checks to make sure the current number is the very first number in it's
            # sequence. For example, we'll ignore a 4 if a 3 already exists in the set, but if not,
            # we'll continue further with the steps directly below
            if (n - 1) not in numSet:
                # This number is the first in the sequence, so it's natural to set its length to 1
                currLen = 1
                # For each number we find consecutively in the sequence, we'll increment the
                # current length by one, and check the next number to see if it exists
                while n + currLen in numSet:
                    currLen += 1
                # Once this has been reached, we've found a full sequence. Now all we need to do is
                # compare it to the longest one we've found so far. If the sequence we found is
                # greater, we'll set the longest sequence to it
                if currLen > out:
                    out = currLen

        # All the info needed has been obtained, all that's left is to return it
        return out