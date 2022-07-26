from collections import deque

n, l, r = map(int,input().split())
graph=[]
dx=[-1,0, 1, 0]
dy=[0,-1, 0, 1]
total_count=0

for _ in range(n):
  graph.append(list(map(int,input().split())))

def process(x,y,index):
  sum = graph[x][y]
  q = deque()
  q.append((x,y))
  count=1
  united=[]
  united.append((x,y))

  while q:
    x, y = q.popleft()
    for i in range(n):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx>=0 and nx<n and ny>=0 and ny<n and union[nx][ny]== -1:
        if
        union[nx][ny] = index
        count+=1
        sum+=graph[nx][ny]
        q.append((nx,ny))
        united.append((nx,ny))

  for x, y in united:
    graph[x][y] = sum//count
  return count
  
  
while True:
  union = [[-1] * n for _ in range(n)]
  index=0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        process(i,j,index)
        index+=1

  if index == n*n:
    break
  total_count+=1    

print(total_count)
      