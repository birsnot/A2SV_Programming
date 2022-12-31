from collections import deque

n, k = list(map(int, input().split()))
theorems = list(map(int,input().split()))
states = list(map(int,input().split()))
q = deque()
ans = 0
total = 0
for i, n in enumerate(theorems):
    total += n*states[i]
for i,state in enumerate(states):
    if state == 0:
        if len(q) < k:
            q.append(theorems[i])
            total += theorems[i]
        else:
            q.append(theorems[i])
            total += theorems[i]-q.popleft()
    else:
        if len(q) < k:
            q.append(0)
        else:
            q.append(0)
            total -= q.popleft()
    ans = max(ans, total)
print(ans)
