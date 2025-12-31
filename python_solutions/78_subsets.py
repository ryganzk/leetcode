''' ***********************************************************************************************
    * Title: 78. Subsets
    * Difficulty: Medium
    * Description: Given an integer array nums of unique elements, return all possible (the power
    * set). The solution set must not contain duplicate subsets. Return the solution in any order.
    * Source: https://leetcode.com/problems/subsets/
    *
    * Verdict: I sought out to solve this problem without using recursion, since I've been using it
    * quite a bit recently for binary tree problems. This ended up taking a bit of time, since my
    * original methods of using a sliding window for backtracking ended up breaking on lists with
    * four or more elements. The new solution is a lot more straightforward, as it iterates
    * through each number in the input list and, for each existing subset in the solution list,
    * creates a new subset by adding the current number.
    * Language: Python
    * Time Complexity: O(n*(2^n))
    * Space Complexity: O(2^n)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-31
    *********************************************************************************************** '''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize solution list with the empty subset
        solutionList = [[]]

        # Iterate through each number in the input list
        for x in nums:
            # Initialize a temporary list to hold new subsets
            subsets = []

            # For each existing subset in the solution list, create a new subset by adding the
            # current number and store it in the subsets list
            for subset in solutionList:
                subsets.append(subset + [x])
            # Extend the solution list with the newly created subsets
            solutionList.extend(subsets)

        # Return the complete list of subsets
        return solutionList