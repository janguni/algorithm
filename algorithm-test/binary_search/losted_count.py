n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

def first_one(array, target, start,end):
  if start > end:
    return 0
  mid = (start+end)//2
  
  if (mid==0 or array[mid-1]<target) and array[mid] == target:
    return mid

  elif array[mid] >= target:
    return first_one(array, target,start,mid-1)
  else:
    return first_one(array, target,mid+1,end)

def last_one(array, target, start,end):
  if start > end:
    return 0
  mid = (start+end)//2
  
  if (mid==n-1 or array[mid+1]>target) and array[mid] == target:
    return mid

  elif array[mid] > target:
    return last_one(array, target,start,mid-1)
  else:
    return last_one(array, target,mid+1,end)


def count_target(n,target,array):
  a = first_one(array,target,0,n-1)
  if a == 0:
    return -1

  b = last_one(array,target,0,n-1)

  return b-a+1
  
print(count_target(n,target,array))