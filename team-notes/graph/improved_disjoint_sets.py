#특정 원소가 포함된 집합(부모) 찾기
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

#두 원소의 집합을 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a<b:
    parent[b] = a
  else:
    parent[a] = b

#노드와 간선의 갯수 받기
v, e = map(int,input().split())
parent = [0] * (v+1)

#부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

#union 연산 수행
for i in range(e):
  a,b = map(int,input().split())
  union_parent(parent,a,b)


#각 원소의 집합 출력
for i in range(1,v+1):
  print(find_parent(parent,i),end=" ")

#각 원소의 집합 출력
for i in range(1,v+1):
  print(parent[i],end=" ")



#마지막에 전체 원소에 대한 find_parent를 돌려줘야
#부모테이블에 가장 부모(?)로 초기화 됨

