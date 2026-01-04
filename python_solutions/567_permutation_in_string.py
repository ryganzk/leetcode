''' ***********************************************************************************************
    * Title: 424. Permutation in String
    * Difficulty: Medium
    * Description: Given two strings s1 and s2, return true if s2 contains a of s1, or false
    * otherwise. In other words, return true if one of s1's permutations is the substring of s2.
    * Source: https://leetcode.com/problems/permutation-in-string/
    *
    * Verdict: I solved this problem using a combination of a dictionary to store the counts of a
    * character occuring in a row, as well as a sliding window to traverse through s2. The logic
    * of what should occur when a character's count drops to zero or when a character not in s1 is
    * encountered took a bit of time to iron out, as the while loop logic took me around 10 minutes
    * to fully debug. A fun problem overall, even though I'm not a big fan of sliding window
    * problems.
    * Language: Python
    * Time Complexity: O(n*m)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2025-12-31
    *********************************************************************************************** '''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initialize character counts dictionary for s1
        initCharCounts = {c: s1.count(c) for c in s1}
        # Initialize current character counts dictionary for s2, ensuring that it starts as a copy of
        # initCharCounts so that modifications to it don't affect the original
        currCharCounts = initCharCounts.copy()
        # Initialize left and right pointers for the sliding window
        left = right = 0

        # Slide the window through s2, stopping once the end is reached
        while right < len(s2):
            # If the current character is not in s1, reset the window and character counts
            if s2[right] not in currCharCounts:
                left = right = left + 1
                currCharCounts = initCharCounts.copy()
            # Else if the current character's count is zero, move the left pointer to the right until
            # the character can be included again
            elif currCharCounts[s2[right]] == 0:
                while currCharCounts[s2[right]] < 1 and left < right:
                    currCharCounts[s2[left]] += 1
                    left += 1
                currCharCounts[s2[right]] -= 1
                right += 1
            # Else, include the current character in the window by decrementing its count
            else:
                currCharCounts[s2[right]] -= 1
                # If the window size matches s1's length, a permutation has been found, so return True
                if right - left + 1 == len(s1):
                    return True
                right += 1

        # If the end of s2 is reached without finding a permutation, return False
        return False
        