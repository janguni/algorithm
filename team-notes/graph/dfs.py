def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v)
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

#2차월 배열 그래프 예시
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)
