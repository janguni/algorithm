from collections import deque
queue = deque()

case = int(input())
for _ in range(case):
  m, n, k = map(int,input().split())
  
  ground = [[0] * n for _ in range(m)]
  
  arr = []
  dx = [-1,0,1,0]
  dy = [0,-1,0,1]
  for _ in range(k):
    x, y = map(int,input().split())
    arr.append((x,y))
  
  count=0
  
  for x, y in arr:
    if ground[x][y]==0:
      count+=1
      queue.append((x,y))
      ground[x][y]=1
  
      while queue:
        x, y = queue.popleft()
  
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
  
          if nx>=0 and nx<m and ny>=0 and ny<n:
            if (nx,ny) in arr and ground[nx][ny]==0:
              queue.append((nx,ny))
              ground[nx][ny]=1
  
  print(count)
      
    