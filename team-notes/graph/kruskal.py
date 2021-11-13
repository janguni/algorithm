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

edges=[]
result = 0 #최종비용

#간선의 비용 받기
for _ in range(e):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

#간선 오름차순 정렬(그리디)
edges.sort()
 
for edge in edges:
  cost, a, b = edge

  #사이클이 아니면 
  if find_parent(parent,a) != find_parent(parent,b): 
    union_parent(parent,a,b)
    result += cost

print(result)


#원리 : 가장 적은 비용의 간선부터 확인하여 사이클이 되지 않을 때 union해주기


