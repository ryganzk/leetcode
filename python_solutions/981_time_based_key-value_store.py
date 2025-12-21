''' ***********************************************************************************************
    * Title: 981. Time Based Key-Value Store
    * Difficulty: Medium
    * Description: A problem that requires building multiple functions to complete. This one
    * utilizes knowledge of dictionaries/maps, as well as how to perform a binary search. What I
    * found was the biggest challenge was handling the key, value, and timestamp all at once, which
    * I found a key-value pair storing a list was the easiest method to do so
    * Source: https://leetcode.com/problems/time-based-key-value-store/
    *
    * Verdict: 
    * Language: Python
    * Time Complexity: O(logn)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-19
    *********************************************************************************************** '''

class TimeMap:

    # Initialization function
    def __init__(self):
        # This problem uses key-value pairsr, so it only makes sense that we initialize a
        # dictionary to store said pairs
        self.keyDict = {}

    # Setter function
    def set(self, key: str, value: str, timestamp: int) -> None:
        # A base case that runs if a key has not been initialized. If it hasn't the key will be set
        # to an empty array for now
        if key not in self.keyDict:
            self.keyDict[key] = []
        # Append a list containing the value and given timestamp to the list referenced by the key
        self.keyDict[key].append([value, timestamp])

    # Getter function
    def get(self, key: str, timestamp: int) -> str:
        # The getter needs a binary search to be ran on the dictionary to achieve a O(logn) time
        # complexity. Therefore we need a left and right pointer pointing the to the values on each
        # end of the key list. The function also needs an output variable to return the correct
        # value once we finish
        l, r = 0, len(self.keyDict.get(key, [])) - 1
        out = ""

        # Repeat until the left iterator is no longer less than or equal to the right iterator
        while l <= r:
            # Calculate the midpoint iterator given the current left and right iterators
            mid = (l + r) // 2
            
            # If the current midpoint points to a timestamp that's less than or equal to the
            # current timestamp, we've folund a valid value to return. Set the output to the number
            # pointed to by the midpoint, and increase the left iterator to the midpoint plus one
            if self.keyDict[key][mid][1] <= timestamp:
                out = self.keyDict[key][mid][0]
                l = mid + 1
            # Else, decrease the right iterator to the midpoint minus one
            else:
                r = mid - 1

        # The value that's closest to the timestamp (but still under or equal to) has been found
        return out