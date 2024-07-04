#!/usr/bin/env python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    def solve(row):
        if row == N:
            result.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    result = []
    board = [-1] * N
    solve(0)
    return result


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


if __name__ == "__main__":
    main()
