''' ***********************************************************************************************
    * Title: 875. Koko Eating Bananas
    * Difficulty: Medium
    * Description: Koko likes to eat slowly but still wants to finish eating all the bananas before
    * the guards return. Return the minimum integer k such that she can eat all the bananas within
    * h hours.
    * Source: https://leetcode.com/problems/koko-eating-bananas/
    *
    * Verdict: I love problems that deal with very niche situations but have a cute backstory to
    * them. Calculating a gorilla's optimal eating speed makes for a more interesting problem than
    * finding a specific number in a generic array. A fun little problem that offers a bit of a
    * challenge with binary searching.
    * Language: Python
    * Time Complexity: O(nlog(max(piles)))
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-19
    *********************************************************************************************** '''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Create left and right iterators representing the amount of BPH (bananas per hour) that
        # Koko can eat, with the left set to 1 (lowest amount) and the right set to the max value
        # of the input piles (highest amount). Also create an output varaible to represent the
        # smallest BPH achievable
        low, high = 1, max(piles)
        out = 0

        # Repeat the steps below as long as the left iterator is less than or equal to the right
        # iterator
        while low <= high:
            # Calculate our middle speed through the left and right iterators, and set the total
            # time needed to eat the banana piles at the current speed equal to zero
            mid, time = (low + high) // 2, 0

            # For every pile found, add the speed it takes to eat the banana pile to the time
            # counter. This requires dividing the pile amount by the speed, and rounding up to the
            # nearest integer (1 hour for 6 bananas at 6BPH, 2 hours for 7 bananas at 6BPH)
            for p in piles:
                time += math.ceil(p / mid)

            # If the time used is lower or equal to the target time, Koko has been able to eat the
            # entire banana pile before the guards return, giving us a valid BPH speed. What we'll
            # do now is update the output variable to the current speed, and lower the right
            # iterator to the current BPH - 1 in order to find a lower speed that meets the target
            # time
            if time <= h:
                out = mid
                high = mid -1

            # Else, Koko has not been able to finish her bananas by the time the guards return,
            # meaning she must work to eat more bananas in a quicker time. We need to raise the
            # current BPH to one over, and repeat the process to find a quicker time
            else:
                low = mid + 1

        # We've found Koko's best BPH so she'll be able to savor her bananas while finishing them
        # before the guards return. Speaking of, return our answer!
        return out