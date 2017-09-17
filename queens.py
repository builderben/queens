#!/usr/bin/env python

import numpy

class Solutions(object):
    def __init__(self, dim):
        self.solution_list = []
        self.dim = dim

    def add(self, board):
        if self._is_unique(board):
            self.solution_list.append(board)

    def _is_unique(self, board):
        for variant in self._variants(board):
            for solution in self.solution_list:
                if numpy.array_equal(variant, solution):
                    return False # Board is not unique
        return True  # Board is unique

    # Get all flipped and rotated variants for comparison
    def _variants(self, board):
        yield(board)                        # identity
        yield(numpy.flipud(board))          # mirrored C
        temp_board = self.dim+1 - board
        yield(temp_board)                   # mirrored R
        yield(numpy.flipud(temp_board))     # mirrored C and R
        temp_board = numpy.array([board.tolist().index(n)+1 for n in range(self.dim, 0, -1)])
        yield (temp_board)                  # 90 degrees
        yield (numpy.flipud(temp_board))    # 90 mirrored C
        temp_board = self.dim+1 - temp_board
        yield(temp_board)                   # 90 mirrored mirrored R
        yield(numpy.flipud(temp_board))     # 90 mirrored mirrored C and R

def test_queens():
    test_board = numpy.array([6,3,5,2,1,4])
    solutions = Solutions(6)
    for test in solutions._variants(test_board):
        print_board(test)

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
