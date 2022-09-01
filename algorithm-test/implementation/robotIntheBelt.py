# 백준 20055(컨베이어 벨트 위의 로봇)
from collections import deque
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())

queue = deque(map(int, sys.stdin.readline().rstrip().split()))
robot=[]
hey=n*2
cnt=1
while True:
  #print("-------------벨트 이동 & 로봇 이동-------------")
  # 벨트 이동
  first = queue.pop()
  queue.appendleft(first)
  robot_len = len(robot)
  # 로봇도 같이 이동
  for i in range(len(robot)):
    dot = robot[i]
    new_dot = dot+1
    robot[i]=new_dot
  if n-1 in robot:
    robot.remove(n-1)

  #print("robot--->", robot)
  
  #print(queue[0],queue[1],queue[2],queue[3])
  #print(queue[7],queue[6],queue[5],queue[4])
  #print()
  
    
  #print("-------------로봇 이동 or 제자리-------------")
  # 로봇들 이동 or 제자리
  for i in range(len(robot)):
    dot = robot[i]
    new_dot = dot+1
    #print("new_dot is ",new_dot)
    if new_dot not in robot and queue[new_dot]>=1 and new_dot<n :
      robot[i] = new_dot
      queue[new_dot]-=1
    elif new_dot>=n-1 and queue[new_dot]>=1:
      queue[new_dot]-=1
  if n-1 in robot:
    robot.remove(n-1)
    #print("robot--->", robot)

  #print(queue[0],queue[1],queue[2],queue[3])
  #print(queue[7],queue[6],queue[5],queue[4])
  #print()

  #print("-------------올리는 위치에 올리기-------------")
  # 올리는 위치에 올리기
  if queue[0]>=1:
    robot.append(0)
    queue[0]-=1
    #print("robot--->", robot)
    
  #print(queue[0],queue[1],queue[2],queue[3])
  #print(queue[7],queue[6],queue[5],queue[4])
  #print()
  
  check=0
  
  # 벨트 전체의 내구도 확인
  for i in range(len(queue)):
    if queue[i]<1:
      check+=1
  if check>=k:
    #print("check is ", check)
    break
  cnt+=1
print(cnt)
      


  
  