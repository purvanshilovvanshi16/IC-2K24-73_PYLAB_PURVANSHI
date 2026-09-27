
matrix = []

print("Enter the elements of the  matrix:")

for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(*row)

total_sum = 0

for i in range(3):
    for j in range(3):
        total_sum += matrix[i][j]

print("\nSum of all elements:", total_sum)

diagonal_sum = 0

for i in range(3):
    diagonal_sum += matrix[i][i]

print("Sum of main diagonal elements:", diagonal_sum)

largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest element:", largest)
print("Smallest element:", smallest)

print("\nTranspose of the matrix:")

for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()