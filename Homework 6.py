import numpy as np

def find_rows_with_min_max_sum(matrix):

  if not matrix or len(set(map(len, matrix))) != 1: 
    return None

  if isinstance(matrix, list):
    matrix = np.array(matrix)

  row_sums = np.sum(matrix, axis=1)
  max_sum_index = np.argmax(row_sums)
  min_sum_index = np.argmin(row_sums)

  return matrix[max_sum_index], matrix[min_sum_index], row_sums[max_sum_index], row_sums[min_sum_index]


matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10,11,12]
]

max_row, min_row, max_sum, min_sum = find_rows_with_min_max_sum(matrix)

if max_row is not None:
  print(f"Строка с наибольшей суммой: {max_row}, Сумма: {max_sum}")
  print(f"Строка с наименьшей суммой: {min_row}, Сумма: {min_sum}")
else:
  print("Ошибка: Матрица пуста или не прямоугольная.")



def transform_matrix(matrix):

  if not matrix:
    return None

  if isinstance(matrix, list):
    matrix = np.array(matrix)

  rows, cols = matrix.shape
  new_matrix = np.copy(matrix)

  for i in range(rows):
    min_val_index = np.argmin(matrix[i])
    min_val = matrix[i, min_val_index]
    new_matrix[i, min_val_index] = 0 if min_val % 2 == 0 else 1

  return new_matrix



matrix2 = [
  [1.5, 2.7, 0.8],
  [4.1, 3.2, 5.9],
  [7.3, 6.1, 9.2]
]

new_matrix2 = transform_matrix(matrix2)
if new_matrix2 is not None:
  print(f"Преобразованная матрица:\n{new_matrix2}")
else:
  print("Ошибка: Матрица пуста.")
