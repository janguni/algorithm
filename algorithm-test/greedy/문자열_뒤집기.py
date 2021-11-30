arr=input()

cnt0=0
cnt1=1

#첫번재 원소 먼저 확인
if arr[0]=='0':
  cnt0+=1
else:
  cnt1+=1

for i in range(1,len(arr)-1):
  if arr[i]!=arr[i+1]: #연속되지 않는 순간이 오면
    if arr[i+1]=='0': #지금까지 1이였다가 0이라는 이야기 이므로
      cnt1+=1 #cnt1이 증가
    else:
      cnt0+=1

print(min(cnt0,cnt1))

