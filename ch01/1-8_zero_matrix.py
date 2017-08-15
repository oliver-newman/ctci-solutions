def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    zero_row = None
    zero_col = None

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if zero_row is None:
                    zero_row = row
                    zero_col = col
                matrix[row][zero_col] = 0
                matrix[zero_row][col] = 0

    if zero_row is None: # No zeros in matrix
        return

    for row in range(1, m):
        if row == zero_row: # Don't overwrite
            continue
        if matrix[row][zero_col] == 0:
            set_row_to_zero(matrix, row)

    for col in range(n):
        if matrix[zero_row][col] == 0:
            set_col_to_zero(matrix, col)

    set_row_to_zero(matrix, zero_row)
        

def set_row_to_zero(matrix, row):
    for col in range(len(matrix[row])):
        matrix[row][col] = 0


def set_col_to_zero(matrix, col):
    for row in range(len(matrix)):
        matrix[row][col] = 0


def test_zero_matrix():
    test_cases = [
        (
            [[1]], 
            [[1]] 
        ),
        (
            [[0, 1], 
             [2, 3]], 
            [[0, 0],
             [0, 3]]
        ),
        (
            [[6, 1, 2], 
             [3, 0, 5], 
             [6, 7, 8]], 
            [[6, 0, 2], 
             [0, 0, 0], 
             [6, 0, 8]] 
        ),
        (
            [[ 0,  1,  2,  3],
             [ 4,  5,  6,  7], 
             [ 8,  9, 10, 11], 
             [12, 13,  0, 15]], 
            [[0, 0, 0,  0],
             [0, 5, 0,  7],
             [0, 9, 0, 11],
             [0, 0, 0,  0]]
        )
    ]
    for case, expected in test_cases:
        zero_matrix(case)
        assert case == expected
