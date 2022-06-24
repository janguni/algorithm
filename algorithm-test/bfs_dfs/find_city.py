from collections import deque

n, m, k, x = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
distanse = [-1] * (n+1)
distanse[x]=0

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

#deque라이브러리를 사용
queue = deque([x])


#큐가 빌 때 까지
while queue:
    now = queue.popleft()

  #해당 원소와 연관된 노드들을 모두 방문
    for next_node in graph[now]:
        if distanse[next_node] == -1:
          #아직 방문하지 않은 노드면 큐에 삽입
            queue.append(next_node)
            distanse[next_node] = distanse[now] +1 


check=False
for i in range(n+1):
    if distanse[i] == k:
        print(i)
        check=True

if check == False:
    print(-1)


  
  