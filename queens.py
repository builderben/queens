#!/usr/bin/env python

import numpy


# Solutions() is used to validate different possible solutions and keep track
# of any valid solutions.
#
# Each solution or test case is represented as a "board", which is a
#  one-dimensional numpy array of integers. The array represents the
#  row position of placed pieces (the index is the column. First row/col = 1.
#
class Solutions(object):
    def __init__(self, dim):
        self.solution_list = []
        self.dim = dim

    def add(self, board):
        if self._is_unique(board):
            self.solution_list.append(numpy.copy(board))

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

    # Prints an ascii representation of a board to the console
    def _print_board(self, board):
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

    # print all solutions
    def print_all(self):
        for board in self.solution_list:
            self._print_board(board)

    # get number of solutions
    def num_solutions(self):
        return (len(self.solution_list))


def solve_queens(pieces=8):
    solutions = Solutions(pieces)
    build_a_board = numpy.array([0 for i in range(0,pieces)])

    # first piece only iterates over half the board. All other soultions
    #  would be mirrored
    for first_row in range(1, int(numpy.ceil(pieces / 2)) + 1):
        build_a_board[0] = first_row
        # remaining pieces will need to test all open spaces
        piece_number = 1
        test_row = 1
        while(piece_number > 0):
            placed_vector = build_a_board[:piece_number]
            while(test_row < pieces+1):
                if test_row not in build_a_board:
                    if not threatened(placed_vector, test_row):
                        # place the piece
                        build_a_board[piece_number] = test_row
                        if piece_number == pieces-1:
                            # check for solution if we just placed the final piece
                            solutions.add(build_a_board)
                            build_a_board[piece_number] = 0
                        break
                test_row += 1
            if build_a_board[piece_number] != 0:  # go to next piece
                piece_number += 1
                test_row = 1
            else:                                 # back to previous piece
                piece_number -= 1
                test_row = build_a_board[piece_number] + 1
                build_a_board[piece_number] = 0

    solutions.print_all()
    print("{} unique solutions found for {} queens.\n".format(solutions.num_solutions(), pieces))

# Checks if any already-placed pieces are threatened diagonally by a new piece in
#  the designated row
def threatened(placed_vector, row):
    threat_check = placed_vector - numpy.array([t for t in range(row+len(placed_vector), row, -1)])
    if 0 in threat_check:
        return True
    threat_check = placed_vector - numpy.array([t for t in range(row-len(placed_vector), row)])
    if 0 in threat_check:
        return True
    return False

if __name__ == "__main__":
    solve_queens(pieces=10)