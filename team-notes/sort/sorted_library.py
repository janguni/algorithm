# sorted()사용
arr1=[7,5,9,0,3,1,6,2,4,8]
result = sorted(arr1)
print(result)


# sort() 사용
arr2 = [7,5,9,0,3,1,6,4,8]
arr2.sort()
print(arr2)


# key를 활용한 sorted
arr3 = [('바나나',2), ('사과', 5), ('당근',3)]
def setting(data):
  return data[1]

result = sorted(arr3, key=setting)
print(result)