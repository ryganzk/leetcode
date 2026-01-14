''' ***********************************************************************************************
    * Title: 9. Palindrome Number
    * Difficulty: Easy
    * Description: Given an integer x, return true if x is a palindrome, and false otherwise.
    * Source: https://leetcode.com/problems/palindrome-number/
    *
    * Verdict: I started out solving this problem using a sliding window approach, but realized
    * that I would need to convert the integer to a string anyways. So instead of that, I tried to
    * solve the problem in a single line, simply by converting the integer to a string and reversing
    * it to see if it matched the original string. This turned out to be a more effective solution
    * overall.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2026-1-4
    *********************************************************************************************** '''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string and check if it reads the same forwards and backwards
        return str(x) == str(x)[::-1]