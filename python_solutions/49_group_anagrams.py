''' ***********************************************************************************************
    * Title: 49. Group Anagrams
    * Difficulty: Medium
    * Description: Given an array of strings strs, group the anagrams together. You can return the
    * answer in any order.
    * Source: https://leetcode.com/problems/group-anagrams/
    *
    * Verdict: A relatively easy problem for its difficulty, at least once I understood how to
    * match anagrams with each other. I'd highly recommend solving 242. Valid Anagram first, as it
    * helps build up an understanding of comparing anagrams with each other
    * Language: Python
    * Time Complexity: O(n*k) (k = length of biggest string)
    * Space Complexity: O(n*k) (k = length of biggest string)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Since we want to group anagrams together, we'll create a dictionary
        sortedDict = {}

        # This for loop will sift through each string given to us by the input array
        for s in strs:
            # The first step is to create a key that represents the final anagram. What I decided
            # do was sort the string in descending alphabetical order, as an easy way to match any
            # possible string given. Keeping in mind that sorted() returns an array, I used the
            # join() function to convert the sorted array into a string
            sort = ''.join(sorted(s))
            # If the newly created key isn't in the dict, create a new entry in the dict, setting
            # the original word to its value
            if sort not in sortedDict:
                sortedDict[sort] = [s]
            # If the newly created key already exists in the dict, append the original word to the
            # current value, thereby adding to the current grouping
            else:
                sortedDict[sort].append(s)
        
        # All of the anagrams given have been sorted in the dictionary, all that's left is to
        # return the array of values
        return sortedDict.values()