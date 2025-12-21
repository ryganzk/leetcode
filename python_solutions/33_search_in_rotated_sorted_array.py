''' ***********************************************************************************************
    * Title: 153. Search In Rotated Sorted Array
    * Difficulty: Medium
    * Description: Given the sorted rotated array nums of unique elements, return the minimum
    * element of this array. You must write an algorithm that runs in O(log n) time.
    * Source: https://leetcode.com/problems/search-in-rotated-sorted-array/
    *
    * Verdict: Given the array nums after the possible rotation and an integer target, return the4
    * index of target if it is in nums, or -1 if it is not in nums. You must write an algorithm
    * with O(log n) runtime complexity.
    * Language: Python
    * Time Complexity: O(logn)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-19
    *********************************************************************************************** '''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        out = nums[l]

        if nums[0] == target:
            return 0

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1