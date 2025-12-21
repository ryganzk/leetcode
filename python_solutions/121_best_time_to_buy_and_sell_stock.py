''' ***********************************************************************************************
    * Title: 121. Best Time to Buy and Sell Stock
    * Difficulty: Easy
    * Description: You are given an array prices where prices[i] is the price of a given stock on
    * the ith day. You want to maximize your profit by choosing a single day to buy one stock and
    * choosing a different day in the future to sell that stock. Return the maximum profit you can
    * achieve from this transaction. If you cannot achieve any profit, return 0.
    * Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    *
    * Verdict: The first LeetCode problem I completed after half a year of absence. Decided to start
    * with a simple sliding window problem, as I consider them to be one of the most fun kinds of
    * problems to solve. And what better way to use them then attempt to solve a semi real-world
    * problem: manipulating the stock market! A fun little problem that everyone should at least
    * attempt to solve.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-9-08
    *********************************************************************************************** '''

import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare variables tracking days of max/min profit, as well as the best profit windows
        # found so far. Min/max days are set to positive/negative infinity to allow for any value
        # on any day, and profit is set to zero since we're not looking to lose money
        minDay, maxDay, profit = math.inf, -math.inf, 0

        # Loop for every value in the prices list
        for x in prices:
            # If we found a day that allows us to buy lower than our current min day, calculate the
            # new profit value, taking the max value of the current profit as well as the values
            # found from subtracting the lowest valued day from the highest in the sequence. Then
            # set both the minimum and maximum profit days to the current day  
            if x < minDay:
                profit = max(maxDay - minDay, profit)
                minDay = x
                maxDay = x
            # Else if the current day can make higher profits than the day currently set to our max
            # profit day, set the max profit day to the current day
            elif x > maxDay: maxDay = x

        # Once the list has been traversed through, return the maximum value of the current profit
        # from the profit made by the minimum and maximum days we currently have in memory
        return max(maxDay - minDay, profit)