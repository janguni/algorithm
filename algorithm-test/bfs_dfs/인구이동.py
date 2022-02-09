from collections import deque

n, l ,r = map(int,input().split())
data=[] #땅에 존재하는 인구수

for i in range(n):
  data.append(list(map(int,input().split())))


dx = [-1,0,1,0]
dy = [0,-1,0,1]

def process(x,y,index):

  united=[] #(x,y)와 연합된 나라의 정보를 담음
  united.append((x,y))
  q=deque() #연합 할 수 있는 나라를 넓이 우선 그래프로 담기
  q.append((x,y))
  union[x][y] = index #연합끼리 구분 index는 현재연합
  sum = data[x][y]
  count = 1 # 현재 연합에 포함된 나라의 수
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >=0 and nx<n and ny>=0 and ny<n and union[nx][ny]==-1:
        term = abs(data[x][y]-data[nx][ny])
        if  term>=l and term<=r:
          q.append((nx,ny))
          #연합에 추가
          union[nx][ny] = index
          united.append((nx,ny))
          count+=1
          sum+=data[nx][ny]
          
  #이번 연합이 끝난 후 인구를 동일하게 분포
  for i, j in united:
    data[i][j] = sum // count

        
#전체 인구 이동수
total_count = 0

while True:
  union = [[-1]* n for _ in range(n)]
  index = 0

  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        process(i,j,index)
        index+=1

  #연합이 없어서 모든 인구 이동이 끝난 경우
  if index ==n*n:
    break

  total_count +=1
  
print(total_count)



