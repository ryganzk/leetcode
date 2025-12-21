''' ***********************************************************************************************
    * Title: 3. Longest Substring Without Repeating Characters
    * Difficulty: Medium
    * Description: Given a string s, find the length of the longest substring without repeating
    * characters.
    * Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    *
    * Verdict: A sliding window problem to determine the longest sequence of non-repeating characters
    * within a string. While it doesn't make for a very interesting problem, I could see it being
    * interesting for analysis purposes, as well as a simple yet somewhat complex problem
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-9-08
    *********************************************************************************************** '''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A very variable declarations are needed: a left index value for our sliding window, a
        # result of the longest sequence we've found so far, and a set to store the current
        # cahracter's we've found
        l, result, charSet = 0, 0, set()
        # Declare the right index value in our for loop, always moving forward until the end is
        # reached
        for r in range(len(s)):
            # If the character represented by the right index is already in our set, remove every
            # element leading up to and including that element from the set, while incrementing the
            # left index a place everytime an element is removed
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Add the new character the right index is on to the set
            charSet.add(s[r])
            # Set the new result to the maximum value of the current result by the different of the
            # right and left index, adding one to that result to account for the offset
            result = max(r - l + 1, result)
        # Once the loop has terminated, return the result
        return result