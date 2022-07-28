n, m = map(int, input().split())
money=[]
INF = 10001
d = [INF] * (m+1)
d[0] = 0


for i in range(n):
  money.append(int(input()))

for k in money:
  for i in range(k, m+1):
    if d[i-k] != INF:
      d[i] = min(d[i], d[i-k]+1)

if d[m]==INF:
  print(-1)
else:
  print(d[m])