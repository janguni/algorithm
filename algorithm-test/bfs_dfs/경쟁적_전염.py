from collections import deque

n, k = map(int,input().split())

graph = []
data =[]

count=0

for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j]!=0:
      data.append((graph[i][j],0,i,j))
      

end,end_x,end_y = map(int,input().split())

#정렬을 하기 위해
#list에 담아놨다가 정렬을 한 다음 queue를 사용
data.sort()
queue = deque(data)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while queue:
  virus, s, x, y = queue.popleft()

  if s==end:
    break
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    #1초에 모든 바이러스가 상하좌우로 증식하므로
    #queue에 1차로 퍼진것, 2차로 퍼진 것을 구분하기위해
    #queue에 초(s)도 추가함
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if graph[nx][ny]==0:
        graph[nx][ny] = virus
        queue.append((virus,s+1,nx,ny))
        

print(graph[end_x-1][end_y-1])
  
  


