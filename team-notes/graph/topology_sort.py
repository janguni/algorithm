from collections import deque

#노드와 간선의 갯수 받기
v,e = map(int,input().split())
#모든 노드의 진입차구 0으로 초기화
indegree = [0] * (v+1)
#인접행렬 초기화
graph = [[] for i in range(v+1)]

#방향 그래프 간선 받기
for i in range(e):
  a, b = map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1 #진입 차수 증가

#위상 정렬 함수
def topology_sort():
  result = [] 
  q=deque()

  #진입차수가 0인 노드 큐에 넣기
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)
  

  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i]-=1
      #진입차수가 0이면 큐에 넣기
      if indegree[i]==0: 
        q.append(i)

  for i in result:
    print(i,end=' ')

topology_sort()




