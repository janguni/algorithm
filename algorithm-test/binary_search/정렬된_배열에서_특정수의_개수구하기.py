n, x = map(int,input().split())
arr = list(map(int,input().split()))

def binary_search(arr,target,start,end):
  if start > end:
    return 0

  mid = (start + end) //2

  if arr[mid] == target:
    return binary_search(arr,target,start,mid-1) + 1 + binary_search(arr,target,mid+1,end)
  elif arr[mid] < target:
    return binary_search(arr,target,mid+1,end)
  else:
    return binary_search(arr,target,start,mid-1)

result = binary_search(arr,x,0,n-1)
if result ==0:
  print(-1)
print(result)
           