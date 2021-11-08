import sys
import heapq
INF=int(1e9)


n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

x,k=map(int,input().split())


def dijkstra(start):
  q=[]
  heapq.heappush(q, (0,start))
  distance[start]=0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: #이미 방문한 노드
      continue
    for i in graph[now]:
      cost = dist+1
      if distance[i]>cost:
        distance[i]=cost
        heapq.heappush(q, (cost,i))

total_dist=0
dijkstra(1)
total_dist+=distance[k]

distance = [INF] * (n+1)
dijkstra(k)
total_dist+=distance[x]

if total_dist<INF:
  print(total_dist)
else:
  print(-1)



    
    





  
