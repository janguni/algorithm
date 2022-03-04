import heapq  #힙 

n = int(input())

h=[]
for _ in range(n):
    heapq.heappush(h,int(input()))

result=0
while len(h)!=1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(h)
    two = heapq.heappop(h)
    sum = one+two
    result+=sum
    heapq.heappush(h,sum)

print(result)
    