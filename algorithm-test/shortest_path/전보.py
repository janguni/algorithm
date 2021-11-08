import heapq

#n:도시 갯수/m:통로 갯수/c:송신 도시 번호
n,m,c=map(int,input().split())
graph=[[] for i in range(n+1)]
INF=int(1e9)
distance=[INF] * (n+1) 



#통로에 대한 정보 받기
for i in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

#다익스크라 알고리즘
def dijkstra(start):
  distance[start] = 0
  q=[]
  heapq.heappush(q,(0,start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  
dijkstra(c)
total=0
count=0

for i in range(n):
  if distance[i]<INF:
    total+=distance[i]
    count+=1

print(count,total)

    


