''' ***********************************************************************************************
    * Title: 74. Search a 2D Matrix
    * Difficulty: Medium
    * Description: Given an integer target, return true if target is in matrix or false otherwise.
    * You must write a solution in O(log(m * n)) time complexity.
    * Source: https://leetcode.com/problems/search-a-2d-matrix/
    *
    * Verdict: A problem that adds another dimension to 704. Binary Search. While reading
    * the problem for the first time, I put it off as it seemed tedious to code, but I am
    * pleasantly surprised that it really wasn't. All the extra dimension did was add another
    * binary search loop, with slightly altered logic. Not really a fun problem, but a worthwhile
    * one to complete if you struggle with binary search type problems
    * Language: Python
    * Time Complexity: O(log(m * n))
    * Space Complexity: O(m * n)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-20
    *********************************************************************************************** '''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Create two iterators, one pointing to the top row of the matrix, and one pointing to the
        # bottom row of the matrix
        top, bottom = len(matrix) - 1

        # Repeat until the top row iterator is no longer less than or equal to the bottom row
        # iterator
        while top <= bottom:
            # Calculate the iterator in the middle of the top and bottom row iterators
            midRow = (top + bottom) // 2
            # If the number at the end of the row in the middle of the current range is less than
            # the target, we can safely rule out the number being in this and and previous rows.
            # Move the top row iterator to point to the next row
            if matrix[midRow][len(matrix[0]) - 1] < target:
                top = midRow + 1
            # Else if the number at the beginning of the row in the middle of the current range is
            # greater than the target, we can safely rule out the number being in this and the
            # following rows. Move the bottom row iterator to point to the previous row
            elif matrix[midRow][0] > target:
                bottom = midRow - 1
            # Else we've found the row in which the target number is on, so break out of the loop
            else:
                break
        
        # Create two iterators, one pointing to the leftmost integer in the row, and one pointing
        # to the rightmost integer in the row
        left, right = 0, len(matrix[midRow]) - 1

        # Repeat until the left column iterator is no longer less than or equal to the right column
        # iterator
        while left <= right:
            # Calculate the iterator in the middle of the left and right column iterators
            midCol = (left + right) // 2
            # If the number pointed to by the middle column iterator is less than the target, the
            # left iterator is moved to point to the number to the right of the middle iterator
            if matrix[midRow][midCol] < target:
                left = midCol + 1
            # Else if the number pointed to by the middle column iterator is greater than the
            # target, the right iterator is moved to point to the number to the left of the middle
            # iterator
            elif matrix[midRow][midCol] > target:
                right = midCol - 1
            # Else, we've found a number that matches the target, meaning all that's left is to
            # return True
            else:
                return True
        
        # We could not find a number that matches the target, so we need to return False
        return False