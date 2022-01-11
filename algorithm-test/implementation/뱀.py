n = int(input()) #맵의 크기 n*n
k = int(input()) #사과 갯수
data = [[0]*(n+1) for _ in range(n+1)] #맵의 정보
info = [] #방향 회전 정보

#맵 초기화(사과 위치 시키기)
for _ in range(k):
  a,b = map(int,input().split())
  data[a][b] = 1 #사과가 있는 곳은 1로 두기

#방향 정보 받기
l = int(input())
for _ in range(l):
  x,c = input().split()
  info.append((int(x),c))

#머리의 방향에 따라 한 칸 이동할 때 행과 열을 어떻게 변화시켜야 할지
#처음에 오른쪽을 보고 있으므로
dx = [0,1,0,-1]
dy = [1,0,-1,0]

#방향바꾸기
def turn(direction,c):
  if c == "L":
    direction = (direction -1) %4
  else:
    direction = (direction +1) %4

  return direction

def simulate():
  x,y = 1,1 #머리 위치
  direction=0
  time = 0
  index = 0 #다음에 회전할 정보
  q = [(x,y)] #뱀이 차지하고 있는 곳(꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][nx]!=2:
      #사과가 없으면 이동 후에 꼬리 제거
      if data[nx][ny]!=1:
        data[nx][ny] = 2
        q.append((nx,ny))
        px,py = q.pop(0)
        data[px][py] = 0
      #사과가가 있다면 이동 후에 꼬리 유지
      else:
        data[nx][ny]=2
        q.append((nx,ny))
    
    #벽이나 몸통과과 부딪혔다면
    else:
      time+=1
      break
    x,y = nx, ny
    time+=1

    if index < l and time == info[index][0]: #첫번째 조건 넣지 않으면 Null임
      direction = turn(direction,info[index][1])
      index+=1
  return time

print(simulate())