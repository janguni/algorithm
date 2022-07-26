n, k = map(int,input().split())
graph=[]
count=[[0]*n for i in range(n)]

for _ in range(n):
  input_list = list(map(int,input().split()))
  graph.append(input_list)

s, x, y = map(int,input().split())

def birus(i,j,graph,count_num):
  nx = [0, -1, 0, 1]
  ny = [-1, 0, 1, 0]

  for t in range(4):
    x = i + nx[t]
    y = i + ny[t]

    if x>=0 and x<n and y>=0 and y<n:
      if graph[x][y]==0 or (graph[x][y]>graph[i][j] and count[x][y]==count_num):
        graph[x][y] = graph[i][j]
        count[x][y] = count_num

for c in range(s):
  for i in range(n):
    for j in range(n):
      if graph[i][j]!=0:
        birus(i,j,graph,c)


print(graph[x-1][y-1])
