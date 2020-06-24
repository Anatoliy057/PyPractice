def check_sort(matrix) -> bool:
    row = len(matrix)
    column = len(matrix[0])
    prev_e = matrix[0][0]
    inc = -1
    i = 1
    j = 0
    while True:
        inc *= -1
        while True:
            print(matrix[i][j])
            if prev_e > matrix[i][j]:
                return False
            prev_e = matrix[i][j]
            i -= inc
            j += inc
            if (0 > i or i >= row) or (0 > j or j >= column):
                i += inc
                j -= inc
                break
        if i == row-1 and j == column-1:
            break
        if i != row-1:
            if i < j:
                if j != column-1:
                    j += 1
                else:
                    i += 1
            else:
                j += 1
        else:
            j += 1
    return True


test_list = [
    [1, 3, 4, 8],
    [2, 5, 7, 9],
    [6, 6, 9, 10]
]
print(check_sort(test_list))
