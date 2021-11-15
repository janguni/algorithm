def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

#학생 번호와 연산갯수 받기
n, m = map(int,input().split())

parent=[0] * (n+1)

#부모를 자기자신으로 초기화
for i in range(n+1):
  parent[i] = i

#연산 수행
for _ in range(m):
  cal, a, b = map(int,input().split())

  #팀합치기 연산
  if cal==0:
    union_parent(parent,a,b)

  #같은 팀 여부 확인
  else:
    if find_parent(parent,a) == find_parent(parent,b):
      print("YES")
    else:
      print("NO")


