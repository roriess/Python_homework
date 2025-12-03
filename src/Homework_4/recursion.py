def is_safe(board, row, col):
    # Checking the column
    for i in range(len(board)):
        if board[i][col]:
            return False

    # Checking the diagonal from top to bottom and from left to right
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c]:
            return False
        r -= 1
        c -= 1

    # Checking the diagonal from top to bottom and from right to left
    r = row
    c = col
    while r >= 0 and c < len(board):
        if board[r][c]:
            return False
        r -= 1
        c += 1

    return True


def generate_boards(row, board, number_of_queens):
    if row == number_of_queens:
        return [board]

    result = []

    for col in range(number_of_queens):
        if is_safe(board, row, col):
            new_board = [row[:] for row in board]
            new_board[row][col] = True
            result.extend(generate_boards(row + 1, new_board))

    return result


def count_of_solutions(number_of_queens):
    board = [[False] * number_of_queens for _ in range(number_of_queens)]
    solutions = generate_boards(0, board, number_of_queens)

    return len(solutions)


print(count_of_solutions(int(input("Enter number of queens: "))))
