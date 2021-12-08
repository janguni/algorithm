arr=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

def rotate_a_matrix_by_90_degree(arr):
  row_len=len(arr) #행길이
  column_len=len(arr[0]) #열길이

  result = [[0] * row_len for _ in range(column_len)] #결과 리스트

  for i in range(row_len):
    for j in range(column_len):
      result[j][row_len-i-1] = arr[i][j]
  
  return result

print(rotate_a_matrix_by_90_degree(arr))