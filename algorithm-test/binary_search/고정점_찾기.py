n = int(input())
arr = list(map(int,input().split()))

def binary_search(arr,start,end):
  if start > end:
    return -1

  mid = (start + end)//2

  if arr[mid]==mid:
    return mid
  #인덱스보다 값이 더 클 경우 오른쪽은 탐색하지 않아도됌
  elif arr[mid]>mid:
    return binary_search(arr,start,mid-1)
  else:
    return binary_search(arr,mid+1,end)
  return -1

print(binary_search(arr,0,n-1))