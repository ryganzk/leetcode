''' ***********************************************************************************************
    * Title: 242. Valid Anagram
    * Difficulty: Easy
    * Description: Given two strings s and t, return true if t is an anagram of s, and false
    * otherwise.
    * Source: https://leetcode.com/problems/valid-anagram/
    *
    * Verdict: For Python code, a dictionary is needed to let the code run in an efficient manner.
    * While a tad simple, even for an easy difficulty, this question is a great introduction to how
    * dictionaries operate, and offers a slight challenge with instantiating key-value pairs
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Out of the gate, we can check to see if the strings are the same length. If they aren't,
        # we can immediately return false, as anagrams MUST share the same characters.
        if len(s) != len(t):
            return False

        # If we get here, our job gets a little more complicated. Using the dictionary class built
        # into Python is the move here, so let's create one for both strings given to us
        sDict, tDict = {}, {}
        
        # For every character we find in the first string, we add one to the dictionary entry of
        # that character. The .get() metod is used here in situations where that character does not
        # exist in the dictionary yet, as the key will be added, the value initializes to zero, and
        # incremented by one
        for c in s:
            sDict[c] = sDict.get(c, 0) + 1
        
        # Do the same for the second string
        for c in t:
            tDict[c] = tDict.get(c, 0) + 1
        
        # If the dictionarys match, then they contain the same amount of the same characters,
        # meaning a valid anagram was found! We've accomplished our mission, so return True
        if sDict == tDict:
            return True
        
        # Looks like the dictionarys didn't match, meaning they do not make a valid anagram. False!
        return False