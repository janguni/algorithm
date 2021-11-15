from collections import deque
import copy

#강의 수 받기
n = int(input())
graph=[[] for i in range(n+1)]
time =[0] * (n+1)
indegree = [0] * (n+1) #진입차수

#강의 정보 받기
for i in range(1,n+1):
  arr = list(map(int,input().split()))
  time[i] = arr[0]
  for x in arr[1:-1]:
    graph[x].append(i)
    indegree[i]+=1

q=deque()
result = copy.deepcopy(time)

#진입차수가 0인 강의 큐에 넣기
for i in range(1,n+1):
  if indegree[i]==0:
    q.append(i)

while q:
  lecture = q.popleft()

  for i in graph[lecture]:
    indegree[i]-=1
    #현재의 값과 lecture을 듣고 현재의 강의를 수강한 것 중
    #큰 시간으로 초기화
    result[i] = max(result[i],result[lecture] + time[i]) 
    if indegree[i]==0:
      q.append(i)

for i in range(1,n+1):
  print(result[i])


  




  






  
