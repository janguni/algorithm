n = int(input())
calendar=[]

for _ in range(n):
  calendar.append(list(map(int,input().split())))
calendar.append(n,0)

max_value=0
for i in range(n-1,-1,-1):
  day = calendar[i][0]+i
  if day <= n:
    calendar[i][1] = max(calendar[day][1] + calendar[i][1],max_value)
    max_value=calendar[i][1]
  else:
    calendar[i][1] = max_value


print(max_value)
  