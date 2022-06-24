n = int(input())
arr = list(map(int,input().split()))

start = 0
end = n-1
result = -1

while start<=end:
  mid = (start + end) // 2

  if mid == arr[mid]:
    result = mid
    break

  elif mid < arr[mid]:
    end = mid-1

  else:
    start = mid+1

print(result)