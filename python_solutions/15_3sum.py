''' ***********************************************************************************************
    * Title: 15. 3Sum
    * Difficulty: Medium
    * Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    * Source: https://leetcode.com/problems/3sum/
    *
    * Verdict: Another problem that I had a deal of difficulty solving, mostly because I believed a
    * solution existed that wasn't in O(n^2) time. Unfortunately, I never managed to find that
    * solution. While I approached this problem using a two pointer approach, I've seen solutions
    * using buckets and hash maps, so this problem seems to offer a variety of approaches
    * Language: Python
    * Time Complexity: O(n^2)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-13
    *********************************************************************************************** '''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting the nums list is an absolute must for this problem. An array of potential 3sums
        # is needed as well for the output array
        nums = sorted(nums)
        out = []
        
        # This first iterator acts as the entry point for our 3sum search. Later in the loop two
        # pointers will be created to search for potential 3sums. As a result, we need to terminate
        # this search before we reach the second-to-last number in the input array, as there won't
        # be any space left to search for 3sums!
        for i in range(len(nums) - 2):
            # If the main pointer points to a number greater than 0, we won't find any more 3sums
            # because no remaining combinations will total 0. Return the output array
            if nums[i] > 0:
                return out
            # If the current pointer is pointing to the same value as it was previously, go to the
            # next number. We don't want to count duplicates, after all!
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # There are no more catch cases to consider, so setup the left pointer directly next to
            # the main pointer, and the right pointer at the last element
            lPntr, rPntr = i + 1, len(nums) - 1

            # Loop through the steps below until the left pointer's value is no longer less than
            # the right pointer's value
            while lPntr < rPntr:
                # Calculate the 3sum of the numbers that have pointers, and check if the value is
                # equal to 0
                threeSum =  nums[i] + nums[lPntr] + nums[rPntr]
                if threeSum == 0:
                    # We've found a valid match, so append the value of these pointers to the
                    # output array
                    out.append([nums[i], nums[lPntr], nums[rPntr]])

                    # Increment the left pointer until a number is found that is not equal to the
                    # number the pointer was previously on. This is done to prevent duplicates from
                    # entering the output array. Also the loop needs to have a clause that prevents
                    # the pointer from moving past the last element in the list
                    lPntr += 1
                    while lPntr < len(nums) and nums[lPntr] == nums[lPntr - 1]:
                        lPntr += 1

                    # Similarly, the right pointer needs to be decremented until a number is found
                    # that is not equal to the number it was previously on. This time, there is a
                    # clause that prevents the pointer from moving past the first element in the
                    # list
                    rPntr -= 1
                    while rPntr > 0 and nums[rPntr] == nums[rPntr + 1]:
                        rPntr -= 1

                # If the 3sum is less than 0, increment the left pointer and try again
                elif threeSum < 0:
                    lPntr += 1
                # Else, the 3sum is greater than 0, so decrement the right pointer and try again
                else:
                    rPntr -= 1

        # We've finished the whole execution, so return the output array
        return out