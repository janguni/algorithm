#가장 긴 증가하는 부분 수열 (Longest Increasing Subsequence)
#수열 D를 주어진 수열길이 만큼 만든다음 1로 모두 초기화
#D[i] = arr[i]를 마지막 원소로 가진 부분 수열의 최대길이 라고 한다
#주어진 수열을 오름차순으로 바꾼 다음 1~n개의 원소를 돌면서
#  0<=j<i D[i] = max(D[i],D[j]+1) if arr[j]<arr[i] 



n=int(input())
arr = list(map(int,input().split()))
arr.reverse()

d=[1]*n

#핵심 알고리즘
for i in range(1,n):
  for j in range(0,i):
    if arr[j]<arr[i]:
      d[i] = max(d[i],d[j]+1)

print(n-max(d))