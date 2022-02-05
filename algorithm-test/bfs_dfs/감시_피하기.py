from itertools import combinations

n= int(input())
#전체 복도
board = []
#선생님
teachers = []
#빈공간(조합을 사용하기 때문에 따로 빼줌)
spaces = []

#정보 입력 받기
for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append((i,j))
    if board[i][j] == 'X':
      spaces.append((i,j))

def watch(x,y,direction):
  
  #왼쪽으로 감시
  if direction==0:
    while y>=0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y-=1

  #오른쪽으로 감시
  if direction==1:
    while y<n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y+=1

  #위쪽으로 감시
  if direction==2:
    while x>=0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x-=1

  #아래쪽으로 감시
  if direction==0:
    while x<n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x+=1


def process():
  #선생님이 있는 곳에서 상하좌우 감시
  for x,y in teachers:
    for i in range(4):
      if watch(x,y,i):
        return True
  return False

find = False

#빈공간 중에서 3개를 선택하는 경우의 수
for data in combinations(spaces,3):
  for x,y in data:
    board[x][y] = 'O'
  
  #학생 감시에 실패한 경우
  if not process():
    find = True
    break
  
  for x,y in data:
    board[x][y] = 'X'

if find:
  print("YES")
else:
  print("NO")
      
  
