from collections import deque
queue = deque()
for i in range(len(queue)):
  print(queue[i])

queue.append(0)
queue.append(1)
queue.append(2)

print(queue)

pop1 = queue.pop()
print("pop1 is ", pop1)
queue.appendleft(pop1)
print(queue)
print(queue[0])


