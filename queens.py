#!/usr/bin/env python

import numpy

def test_queens():
    test_board = numpy.array([2, 4, 1, 3])
    print_board(test_board)

# Prints an ascii representation of the board to the console
#   board = list or one-dimensional numpy array of integers, representing the
#           row position of the pieces (the index is the column. First row/col = 1.
#           Numbers beyond the dimensions of the board are not printed.
def print_board(board):
    dims = len(board)
    print("\n{}".format(board))
    for row in range(1,dims+1):
        rowstring=""
        for col in board:
            if col == row:
                rowstring += " x "
            else:
                rowstring += " - "
        print(rowstring)

if __name__ == "__main__":
    test_queens()
