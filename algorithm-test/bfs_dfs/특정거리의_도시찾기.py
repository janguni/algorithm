from collections import deque

def bfs(start,last_step,graph,visited):
    step=1

    q = deque([start])
    visited[start] = True
    result=[]
    stop=False
  
    while q:
        if step==last_step:
            stop = True

        v = q.popleft()


        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                if stop:
                    result.append(i)
    
        if stop:
            if len(result)!=0:
                sorted(result)
                for i in result:
                    print(i)
                break
        else:
            step+=1
    if len(result) == 0:
        print(-1)



n, m, k, x = map(int,input().split())
graph=[[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

visited = [False] * (n+1)

bfs(x,k,graph,visited)




  
          
        


    




