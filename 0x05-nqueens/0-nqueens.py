#!/usr/bin/python3
"""This program solves the N queens problem."""
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the specified row
    and column on the chessboard.

    Args:
    board (list of lists): The chessboard state.
    row (int): The row where the queen is to be placed.
    col (int): The column where the queen is to be placed.

    Returns:
    bool: True if it is safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
    n (int): The size of the chessboard and the number of queens to place.

    Prints:
    List of solutions, where each solution is a list of queen positions.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []

    def solve(row):
        if row == n:
            solutions.append([[i, row.index(1)]
                              for i, row in enumerate(board)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
