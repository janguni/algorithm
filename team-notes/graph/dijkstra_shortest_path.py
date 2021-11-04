import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 10으로 설정

#노드, 간선 갯수 받기
n,m = map(int,input().split())
#시작하는 노드 받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 리스트 생성
graph = [[] for i in range(n+1)]
#최단거리 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))


def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start)) #시작 노드까지의 거리는 0으로 설정
  distance[start]=0
  while q: #큐가 비지 않을 때까지
    dist,now = heapq.heappop(q)
    if distance[now]<dist: #원래의 거리가 더 짧으면 이미 방문한 것으로 간주
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]: #현재의 거리가 더 짧으면 
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0])) #큐에 갱신


#다익스크라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
