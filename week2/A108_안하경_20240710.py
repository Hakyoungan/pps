def transpose(matrix):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return []
    
    # Number of rows and columns in the input matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Create the transposed matrix with dimensions (cols, rows)
    transposed_matrix = [[0] * rows for _ in range(cols)]
    
    # Fill the transposed matrix with appropriate values
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

# Example 1
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Input:", matrix1)
print("Output:", transpose(matrix1))

# Example 2
matrix2 = [[1, 2, 3], [4, 5, 6]]
print("Input:", matrix2)
print("Output:", transpose(matrix2))
