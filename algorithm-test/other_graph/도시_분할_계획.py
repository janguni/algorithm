def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

#집과 길의 갯수 받기
n, m = map(int,input().split())
parent = [0] * (n+1)
edges = [] #길의 정보
result = 0 #최종 길의 유지비용
last_cost = 0

#부모를 자기자신으로 초기화
for i in range(1,n+1):
  parent[i] = i

#길의 유지비 받기
for _ in range(m):
  a ,b ,cost = map(int,input().split())
  edges.append((cost,a,b))
  
#길의 유지비용을 오름차순으로 정렬
edges.sort()

#신장트리 형성
for edge in edges:
  cost,a,b = edge
  if (find_parent(parent,a)!=find_parent(parent,b)): #사이클이 아니면
    union_parent(parent,a,b)
    result += cost
    last_cost=cost

print(result-last_cost)


    





