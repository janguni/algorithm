arr=list(map(int,input()))
result=0

#첫번째, 두번째 숫자 먼저 연산
if arr[0]<=1 or arr[1]<=1:
  result=arr[0]+arr[1]
else:
  result=arr[0]*arr[1] 


for i in range(2,len(arr)):
  if result<=1 or arr[i]<=1:    #0,1만 아니면 *가 우선
    result+=arr[i]
  else:
    result*=arr[i]

print(result)
