n, x = map(int,input().split())
arr = list(map(int,input().split()))

def first(arr,target,start,end):
  if start > end:
    return None

  mid = (start + end) //2

  #target인 숫자들 중 가장 왼쪽인 인덱스 반환
  if target==arr[mid] and (mid==0 or target>arr[mid-1]):
    return mid
  #mid이 target보다 크거나 같으면 왼쪽 탐색
  elif target <= arr[mid]:
    return first(arr,target,start,mid-1)
  else:
    return first(arr,target,mid+1,end)

def last(arr,target,start,end):
  if start > end:
    return None

  mid = (start + end) //2

  #target인 숫자들 중 가장 오른쪽인 인덱스 반환
  if target==arr[mid] and (mid==n-1 or target<arr[mid+1]):
    return mid

  elif target >= arr[mid]:
    return last(arr,target,mid+1,end)
  else:
    return last(arr,target,start,mid-1)

def count_by_value(arr,x):
  n = len(arr)

  a= first(arr,x,0,n-1)
 
  if a == None:
    return 0
    
  b = last(arr,x,0,n-1)
  
  return b-a+1

count = count_by_value(arr,x)

if count == 0:
  print(-1)
else:
  print(count)

  