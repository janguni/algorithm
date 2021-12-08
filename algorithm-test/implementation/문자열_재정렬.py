arr=input()
alpha=[]
sum=0
print(arr)
for x in arr:
  if x.isalpha():
    alpha.append(x)
  else:
    sum+=int(x)

alpha.sort()
if sum!=0:
  alpha.append(str(sum))

print(''.join(alpha))
