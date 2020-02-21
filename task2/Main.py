def to_matrix(arr: list) -> list:
    matrix = arr
    matrix.sort(key=len, reverse=True)
    i = 0
    while i < len(matrix):
        if len(matrix[i]) <= i:
            break
        i += 1
    print(i)
    matrix = matrix[:i]
    j = 0
    while j < i:
        matrix[j] = matrix[j][:i]
        j += 1
    return matrix


two_array = [
    [1, 2, 3, 4],
    [4, 5, 6],
    [7, 8, 9, 9, 9],
    [1, 1, 1, 1]
]
print(to_matrix(two_array))
