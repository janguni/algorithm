#입력
n = int(input())
stages=list(map(int,input().split()))
answer=[]
length = len(stages) # 총 사람 수
     
for i in range(1, n+1): #스테이지 번호
  count = stages.count(i) #해당 스테이지에 사람이 몇 명 있는지
        
  if length == 0: # 더이상 도전한 사용자가 없음
    fail=0 # 그러면 해당 스테이지에는 실패율이 0
  else:
    fail = count / length
            
  answer.append((i,fail))
  length-=count
  
answer = sorted(answer,key = lambda t: t[1], reverse = True) 
answer = [i[0] for i in answer]
print(answer)
  