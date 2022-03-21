n = int(input())
graph=[]

for _ in range(n):
  graph.append(list(map(int,input().split())))

for i in range(n):
  for j in range(len(graph[i])):
    left=0
    right=0
    if i-1>=0 and j-1>=0:
      left=graph[i-1][j-1]
    if i-1>=0 and j<i:
      right=graph[i-1][j]
    graph[i][j] = graph[i][j] + max(left,right)

result = max(graph[n-1])
print(result)

