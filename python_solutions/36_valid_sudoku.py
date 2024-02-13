''' ***********************************************************************************************
    * Title: 36. Valid Sudoku
    * Difficulty: Medium
    * Description: Determine if a 9 x 9 Sudoku board is valid.
    * Source: https://leetcode.com/problems/valid-sudoku/
    *
    * Verdict: I felt the problem looked much more daunting that it actually is. Since the problem
    * calls for checking the AVAILABLE numbers if it's valid, and not if it's solvable, things are
    * made significantly easier. The real challenge is scanning each position on the board once and
    * only once, which led me to enjoy coming up with potential solutions far more than I normally
    * would
    * Language: Python
    * Time Complexity: O(1)
    * Space Complexity: O(1)
    *
    * Author: Ryan Ganzke
    * Date: 2024-2-12
    *********************************************************************************************** '''

class Solution:
    # A helper function I created to determine the box the current number falls within. Since each
    # box contains three elements in each row and column before moving to the next, we perform an
    # integer divide on each iterator, and add them together to get the box number. Before this
    # though, we need to multiply the resulting first integer equation by three, as lower boxes are
    # valued three times more than boxes higher than it
    def boxCalc(self, iter1: int, iter2: int) -> int:
        return 3 * (iter1 // 3) + (iter2 // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # To start off, we need to create 27 dictionaries: 9 to account for the rows, 9 to account
        # for the columns, and 9 to account for the boxes. These are stored in respective row/col/
        # box dicts for ease of reference later
        rowDicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        colDicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        boxDicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        # Iterates through every row
        for i in range(9):
            # Iterates through every column
            for j in range(9):
                # Stores the resulting element, so we don't need to call the input array for the
                # remaining steps
                n = board[i][j]

                # It is possible that n is a period, meaning that that position in the sudoku is
                # empty. This means we don't need to check it, so we check the next position
                # instead
                if n.isnumeric():
                    # Calls the helper function defined above to get the box the number resides in
                    box = self.boxCalc(i, j)

                    # Checks to see if any of the corresponding row, column, or box dicts contains
                    # the specified number. If they do, this means a repeat was found, and
                    # therefore the given board is not valid. Return False!
                    if (n in rowDicts[i].keys() or n in colDicts[j].keys() or
                        n in boxDicts[box].keys()):
                        return False
                    # If this has been reached, no duplicate values were found in the appropriate
                    # dictionaries. In that case, add the number to these dictionaries, and pray
                    # we don't find an overlapping value in the future
                    else:
                        rowDicts[i][n] = ""
                        colDicts[j][n] = ""
                        boxDicts[box][n] = ""

        # Great news, the sudoku has been tested and is a valid board! Return True!
        return True