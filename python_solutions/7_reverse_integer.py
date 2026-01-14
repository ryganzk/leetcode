''' ***********************************************************************************************
    * Title: 7. Reverse Integer
    * Difficulty: Medium
    * Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing
    * x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return
    * 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    * Source: https://leetcode.com/problems/reverse-integer/
    *
    * Verdict: I had to extend my original solution to account for integers over the 32-bit range,
    * but asides from that, this problem was fairly straightforward. Considering I just finished
    * problem 9 beforehand, I already had the idea of converting the integer to a string and
    * reversing its characters fresh in my mind, so implementing the rest wasn't too tricky.
    * Language: Python
    * Time Complexity: O(n)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2026-1-13
    *********************************************************************************************** '''

class Solution:
    def reverse(self, x: int) -> int:
        # Create variables that hold the string representation of the integer and the reversed
        # integer
        xStr, xRev = str(x), ""

        # If the integer is negative, reverse the digits after the negative sign, else reverse all
        # digits normally
        if xStr[0] == '-':
            xRev = -int((str(x)[1:])[::-1])
        else:
            xRev = int(str(x)[::-1])

        # If the reversed integer is outside the 32-bit signed integer range, return 0, else return
        # the reversed integer as is
        if xRev < -2 ** 31 or xRev > 2 ** 31 - 1:
            return 0
        return xRev
        