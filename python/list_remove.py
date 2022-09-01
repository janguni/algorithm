arr=[0,3,7,9]
for i in range(len(arr)):
  print(i,"번째의 값은 ", arr[i])
print("==========================")

arr.remove(3)
for i in range(len(arr)):
  print(i,"번째의 값은 ", arr[i])
print("==========================")

arr.append(10)
for i in range(len(arr)):
  print(i,"번째의 값은 ", arr[i])
print("==========================")

