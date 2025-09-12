matrix = (6,5, -8,-100,15,17,9,51, 22,45)
digit1 = None
digit2 = None
minimumSum = 10000000000


for i in range(len(matrix)):
    for j in range(len(matrix) - 1):
        if(matrix[i] == matrix[j]):
            continue
        if( abs(minimumSum) > abs(matrix[i]+matrix[j])):
            digit1 = matrix[i]
            digit2 = matrix[j]
            minimumSum = digit1 + digit2;

print("Sum: ", minimumSum)
print("Digit 1: ", digit1)
print("Digit 2: ", digit2)