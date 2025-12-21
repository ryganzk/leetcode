''' ***********************************************************************************************
    * Title: 347. Top K Frequent Elements
    * Difficulty: Medium
    * Description: Given an integer array nums and an integer k, return the k most frequent
    * elements. You may return the answer in any order.
    * Source: https://leetcode.com/problems/top-k-frequent-elements/
    *
    * Verdict: One of the first questions I started to struggle a little on (keep in mind this was
    * my eighth or ninth question). While creating a dictionary of sorted values is nothing
    * special, the real challenge kicks in with extracting the keys with the highest values. An
    * interesting problem that I could see having a potential real-world application
    * Language: Python
    * Time Complexity: O(nlogn)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This problem is going to require space for two objects: a dictionary to determine the
        # occurance of each number in the input array, and an output array
        count = {}
        out = []

        # For each number we find, we'll increase the value of its corresponding key by one. For
        # numbers that do not have a key let, we'll use the get() method to instantiate the
        # key-value pair, and set the value equal to 1
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Okay this line is a bit more complicated, but what it does is use the sorted() method on
        # the count dictionary to spit out an array of the key-value pairs, with the highest values
        # at the top of the list. To do this, we set the sort condition to the value (done through
        # the lambda expression for key), and set reverse equal to true so the highest values
        # appear at the top
        sortCount = sorted(count.items(), key=lambda it: it[1], reverse=True)

        # Now we add the first k values to the output list, essentially giving up a list of the top
        # k most frequent elements
        for n in range(k):
            out.append(sortCount[n][0])

        # Return the output array
        return out