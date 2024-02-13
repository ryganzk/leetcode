''' ***********************************************************************************************
    * Title: 125. Valid Palindrome
    * Difficulty: Easy
    * Description: Given a string s, return true if it is a palindrome, or false otherwise.
    * Source: https://leetcode.com/problems/longest-consecutive-sequence/
    *
    * Verdict: I think the problem wants you to use two pointers to move down the palindrome, but
    * at least in Python, it's much simpler to "clean" the string of all non-alphanumeric
    * characters, and compare the string with the reversed string. With this one, I wanted to flex
    * my regex skills to perform the clean in a single line
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using the re library imported above, use the substitution method on the input string to
        # strip it of all non-alphanumeric characters. The regex "^a-zA-Z0-9" is pretty simple, the
        # beginning carrot matches with the beginning of the input, and a-zA-Z0-9 states that the
        # resulting string can only be made up of alphanumeric characters. Finally, we set all
        # uppercase characters to lowercase to help with the below comparison
        palindrome = re.sub(r'[^a-zA-Z0-9]', "", s).lower()

        # Returns the result of the string compared to its reverse. If the strings are equal to
        # each other, that means the string is a valid palindrome, and True will be returned. If
        # the strings do not match, it's not a palindrome, and False will be returned
        return palindrome == palindrome[::-1]