def matrix_addition(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Same dimension wala matrix do! ")
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

def matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("MUST BE no of rows = no of column! try again bud")
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        
        for j in range(len(matrix_b[0])):
            total = 0
            for k in range(len(matrix_b)):
                total += matrix_a[i][k] * matrix_b[k][j]
            row.append(total)
        result.append(row)
    return result
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)

matrix3 = [[1, 2], [3, 4]]
matrix4 = [[5, 6], [7, 8]]
print("Matrix Addition:", matrix_addition(matrix3, matrix4))
print("Matrix Multiplication:", matrix_multiplication(matrix1, matrix2))