# 퀵 정렬 예시
arr= [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
  if len(arr)<=1: # 리스트가 하나 이하의 원소만을 담으면 종료
    return arr

  pivot = arr[0] # 피벗
  tail = arr[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x<=pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x >pivot] # 분할된 오른쪽 부분

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))
 
