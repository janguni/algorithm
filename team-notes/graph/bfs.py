from collection import deque

def bfs(graph,start,visited):
  
  #deque라이브러리를 사용
  queue = deque([start])
  visited[start] = True

  #큐가 빌 때 까지
  while queue:
    v = queue.popleft()
    print(v,end=" ")

    #해당 원소와 연관된 노드들을 모두 방문
    for i in graph[v]:
      if not visited[i]:
        #아직 방문하지 않은 노드면 큐에 삽입
        queue.append(i)
        visited[i] = True
  

