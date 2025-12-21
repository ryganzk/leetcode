''' ***********************************************************************************************
    * Title: 853. Car Fleet
    * Difficulty: Medium
    * Description: Return the number of car fleets that will arrive at the destination.
    * Source: https://leetcode.com/problems/car-fleet/
    *
    * Verdict: A problem that stumped me far more than it should've. I thought of multiple
    * approaches, such as using a stack to store and pop off position/speed pairs. In the end, I
    * used a dictionary, as Python makes it eay to create associations between two values. After
    * that, all that was needed was a simple descending sort and comparisons to determine which
    * cars form a fleet
    * Language: Python
    * Time Complexity: O(nlogn)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-17
    *********************************************************************************************** '''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Our problem utilizes a dictionary for storing position/speed pairs, and an output list
        # for returning the result of the calculations
        fleetDict, out = {}, []

        # Populates our dictionary, using the position of the car as our key, and the speed of the
        # car as the entry's value
        for i in range(len(position)):
            fleetDict[position[i]] = speed[i]

        # Sort the position array in descending order. This way, we can take care of cars that are
        # closest to their destination first, and see if there are any cars behind it that will
        # join its fleet
        position = sorted(position, reverse = True)

        # For every car position we have, we'll calculate the amount of time it would take to reach
        # the target destination, calculated by subtracting the position by the target to find the
        # distance, and dividing that by its speed (stored in the dictionary) to calculate the time
        # needed
        for p in position:
            time = (target - p) / fleetDict[p]

            # If it takes longer to reach the destination than the last car, which will be the last
            # element in our output list, append the time to the input list, where it is now the
            # current last fleet to reach the destination. Remember to have a base case that checks
            # to make sure the output list is empty!
            if p == position[0] or time > out[-1]:
                out.append(time)

        # The result has been obtained, so return the output
        return len(out)