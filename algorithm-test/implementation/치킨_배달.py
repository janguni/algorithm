n, m = map(int,input().split())
city=[]
chicken=[]

for i in range(n):
  city.append(list(map(int,input().split())))

def chicken_distance(r,c,city):

  for i in range(n):
    for j in range(n):
      if city[i][j]==2: # 치킨집이라면
        distance = min(abs(r-i) + abs(c-j),distance)
        chicken_row = i #가장 가까운 치킨집 행
        chicken_col = j #가장 가까운 치킨집 열
  chicken.append([i,j])
  chicken
  
  return distance

      


