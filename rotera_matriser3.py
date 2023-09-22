def print_matrix(matrix):
   for row in matrix:
      print(row)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]
print_matrix(matrix)
print()
nums_rows = len(matrix)
nums_cols = len(matrix[0])
transpose_matrix = []

for i in range(nums_rows):
  new_row = []
  for j in range(nums_cols):
    new_row.append(matrix[j][i])

  transpose_matrix.append(new_row)

print_matrix(transpose_matrix)
reversed_matrix = []

for row in transpose_matrix:
    reversed_rows = list(reversed(row))
    reversed_matrix.append(reversed_rows)
print()
print_matrix(reversed_matrix)