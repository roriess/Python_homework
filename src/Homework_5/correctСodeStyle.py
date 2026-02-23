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


total_count = 0


def backtrack(board, row, number_of_queens):
    global total_count

    if row == number_of_queens:
        total_count += 1
        return

    # Trying to place a queen in each column of the current row
    for col in range(number_of_queens):
        if is_safe(board, row, col):
            board[row][col] = True
            backtrack(board, row + 1, number_of_queens)
            board[row][col] = False


def count_of_solutions(number_of_queens):
    board = [[False] * number_of_queens for _ in range(number_of_queens)]

    backtrack(board, 0, number_of_queens)

    return total_count


print(count_of_solutions(int(input("Enter number of queens: "))))
