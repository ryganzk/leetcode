''' ***********************************************************************************************
    * Title: 1. Two Sum
    * Difficulty: Easy
    * Description: Given an array of integers nums and an integer target, return indices of the two
    * numbers such that they add up to target.
    * Source: https://leetcode.com/problems/two-sum/
    *
    * Verdict: One of Leetcode's most famous problems, and it shows. For an easy problem, coming up
    * with a solution was exciting because there were so many angles to consider, and so many
    * possible solutions. The one I came up with might not neccesarily be the one someone else
    * finds, and I find it beautiful that this level of flexibility exists
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using a dictionary will yield the easiest solution
        solDict = {}

        # This will be a little tricky to explain. We'll start out iterating through the index of
        # every element in the range of the given array
        for i in range(len(nums)):
            # If we see that the current number is in the dict, we will return the value of the
            # matching key, followed by the index of the current element in the array
            if nums[i] in solDict.keys():
                return [solDict[nums[i]], i]
            # If the current number is not a key in the dict, we'll add a key that matches the
            # result of the target subtracted by the current number. Essentially, we'll add the
            # number we're looking for to complete the two square. As an example, if the current
            # number we have is a 3, we'd be looking for a 6. If the 6 has not been found yet, we
            # add the 6 to the dict in hopes we find it in the future. Lastly, we add the index
            # of the current number as the key's value, so we can call it back in the result if
            # the match is found in the future
            else:
                solDict[target - nums[i]] = i