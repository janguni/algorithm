n=int(input())
degree=list(map(int,input().split())) #각 모험가의 공포도

#오름차순 정렬
degree.sort() 

group=0 # 같이 떠나는 각 그룹의 모험가 수
result=0 #총 그룹의 수
for i in degree:
  group+=1

  if group>=i:
    result+=1
    group=0

print(result)


