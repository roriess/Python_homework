import itertools


def is_safe(queen_positions):
    number_of_queens = len(queen_positions)

    for i in range(number_of_queens):
        for j in range(i + 1, number_of_queens):
            if queen_positions[i] == queen_positions[j] \
               or abs(queen_positions[i] - queen_positions[j]) == abs(i - j):
                return False

    return True


def count_of_solutions(number_of_queens):
    '''
    The index of a queen - column position on the chessboard,
    and its value - the row position on the chessboard.
    '''
    rows = list(range(number_of_queens))

    possible_positions = itertools.permutations(rows)

    count = sum(1 for pos in possible_positions if is_safe(pos))

    return count


print(count_of_solutions(int(input("Enter number of queens: "))))
