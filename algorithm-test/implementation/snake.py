from collections import deque

n = int(input())
board=[[-1] * (n+1) for _ in range(n+1)] # n*n 보드

k = int(input()) # 사과 갯수
for _ in range(k):
  x,y = map(int,input().split())
  board[x][y]=2 # 사과

l = int(input()) # 방향 수
directions=[]
for _ in range(l):
  sec, direction = input().split()
  sec = int(sec)
  directions.append((sec, direction))

# 좌, 상, 우, 하
dx=[0,-1,0,1]
dy=[-1,0,1,0]

count=0 # 시간
board[1][1]=1 # 뱀이 있음
i=2 # 방향의 시작은 오른쪽
queue = deque()
queue.append((1,1)) #꼬리
x=1
y=1
while True:
  count+=1
  # 뱀의 머리가 한 칸 이동
  x = x + dx[i]
  y = y + dy[i]
  #print("(",x,",",y,")")

  if (x>=1 and x<=n and y>=1 and y<=n) == False: # 벽에 닿음
    #print(count,"초에 벽에 닿음")
    break

  elif board[x][y]==1 or (x,y) in queue: # 뱀의 몸에 닿으면
    #print(count,"초에 뱀의 몸에 닿음")
    break
    
  elif board[x][y] ==2 : # 사과가 있으면
    board[x][y]=1
    queue.append((x,y))
    
  else: # 사과가 없음
    queue.append((x,y))
    tx, ty = queue.popleft()
    board[tx][ty]=-1
    #print(tx,ty,"----꼬리 뺌")

  if (count,'D') in directions:
    #print(count,"가 지나서 오른쪽으로 이동")
    i = (i+1) % 4
  if (count,'L') in directions:
    #print(count,"가 지나서 왼쪽으로 이동")
    i = (i-1) % 4

print(count)

    
    


    
  

