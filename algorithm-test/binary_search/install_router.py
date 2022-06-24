n, c = list(map(int,input().split()))
array=[]
for i in range(n):
    num = int(input())
    array.append(num)
array.sort()


def binary_search(start,end):
  while start<=end:
    count=1
    current = array[0]
    mid = (start + end)//2
        
    for i in range(1,n):
      if array[i] >= current + mid:
        count+=1
        current = array[i]

    if count>=c: 
      global answer
      start=mid+1
      answer = mid  # 업그레이드
      
    else:
      end=mid-1
    
answer = 0
binary_search(1, array[-1]-array[0])
print(answer)
    

        
        
        
        