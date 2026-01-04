''' ***********************************************************************************************
    * Title: 424. Longest Repeating Character Replacement
    * Difficulty: Medium
    * Description: You are given a string s and an integer k. You can choose any character of the
    * string and change it to any other uppercase English character. You can perform this operation
    * at most k times. Return the length of the longest substring containing the same letter you
    * can get after performing the above operations.
    * Source: https://leetcode.com/problems/longest-repeating-character-replacement/
    *
    * Verdict: This one gave me more problems than I thought it would. I went through two iterations:
    * the first one used a heap, but unfortunately Leetcode didn't accept it as it caused a time
    * limit exceeded error for the larger test cases. This second iteration used a sliding window
    * approach paired with a frequency array, which ended up being much more efficient.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-31
    *********************************************************************************************** '''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # If the string is empty, return 0
        if not s:
            return 0
        
        # Initialize frequency array, left pointer, max frequency, and result
        count = [0] * 26
        left, maxFreq, result = 0, 0, 0

        # Iterate through the string with the right pointer
        for right in range(left, len(s)):
            # Update the frequency array and max frequency for the current character, increasing the
            # count for the character and updating maxFreq if necessary
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            maxFreq = max(maxFreq, count[idx])

            # If the current window size minus the max frequency exceeds k, shrink the window from
            # the left side by decrementing the count of the character at the left pointer and moving
            # the left pointer to the right
            while (right - left + 1) - maxFreq > k:
                leftIdx = ord(s[left]) - ord('A')
                count[leftIdx] -= 1
                left += 1

            # Update the result with the maximum window size found so far
            result = max(result, right - left + 1)

        # Once the iteration is complete, return the result
        return result
