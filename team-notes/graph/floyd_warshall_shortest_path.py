INF = int(1e9)

n = int(input()) #노드의 갯수 받기
m = int(input()) #간선의 갯수 받기
#2차원 그래프를 모두 무한으로 초기화
graph = [[INF] *(n+1) for i in range(n+1)]

#자기자신에서 자신까지 가는 거리는 0으로 설정
for a in range(1,n+1):
  graph[a][a]=0

#각 간선의 정보를 받아서 초기화
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a][b]=c

#플로이드 워셜 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INFINITY", end = " ")
    else:
      print(graph[a][b], end=" ")
  print()
