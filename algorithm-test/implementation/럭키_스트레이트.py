arr=list(map(int,input()))

left_sum=0 #왼쪽 부분의 합
right_sum=0 #오른쪽 부분의 합

for i in range(0,len(arr)//2):
  left_sum+=arr[i]
  right_sum+=arr[len(arr)-1-i]

if left_sum == right_sum:
  print("LUCKY")
else:
  print("READY")
