''' ***********************************************************************************************
    * Title: 242. Longest Repeating Character Replacement
    * Difficulty: Medium
    * Description: You are given a string s and an integer k. You can choose any character of the
    * string and change it to any other uppercase English character. You can perform this operation
    * at most k times. Return the length of the longest substring containing the same letter you
    * can get after performing the above operations.
    * Source: https://leetcode.com/problems/longest-repeating-character-replacement/
    *
    * Verdict: 
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return