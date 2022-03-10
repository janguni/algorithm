n,c = list(map(int,input().split()))

arr=[]
for _ in range(n):
  arr.append(int(input()))

#이분 탐색을 위한 정렬
arr.sort()

start = 1 #min gap
end = arr[-1] - arr[0] # max gap
result=0

#최적의 gap을 이분탐색으로 찾음
while(start <= end):
  mid = (start + end)//2
  count=1 #arr[0]는 이미 공유기 설치
  value = arr[0] #현재 가장 왼쪽에 있는 공유기 위치

  for i in range(1,n): #공유기 설치
    if arr[i] >= value+mid:
      value = arr[i]
      count+=1

  if count>=c: #c개 이상의 공유기를 설치 할 수 있는 경우
    start=mid+1
    result=mid #최적의 결과 저장

  else:
    end = mid-1

print(result)