n, m = map(int, input().split())
arr = [0 for i in range(1,11)]

num=list(map(int,input().split()))

for n in num:
  arr[n]+=1

result=0
for i in range(1,m):
  if i!=0:
    sum=0
  else: continue

  for j in range(i+1,m+1):
    if j!=0:
      sum+=(arr[j]*arr[i])
  result+=sum


print(result)
      


