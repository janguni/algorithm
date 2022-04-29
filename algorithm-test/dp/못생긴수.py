n = int(input())

ugly = [0] * n
ugly[0] = 1

#2배, 3배, 5배를 위한 인덱스
i2=i3=i5=0

#각 배수의 초기값
next2, next3, next5 = 2,3,5

#1부터 n까지 못생긴 수 찾기
for k in range(1,n):
  ugly[k] = min(next2, next3, next5)

  if ugly[k] == next2:
    i2+=1
    next2 = ugly[i2] * 2

  if ugly[k] == next3:
    i3+=1
    next3 = ugly[i3] * 3

  if ugly[k] == next5:
    i5+=1
    next5 = ugly[i5] * 5

print(ugly[n-1])

