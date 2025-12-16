from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
N=int(input().strip())
M=int(input().strip())
dic=defaultdict(list)
vis=[False]*(N+1)
for i in range(M):
    u, v=map(int, input().strip().split())
    dic[u].append(v)
    dic[v].append(u)
dq=deque([1])
answer=-1
while dq:
    tmp=dq.popleft()
    if vis[tmp]:
        continue
    vis[tmp]=True
    answer+=1
    for i in dic[tmp]:
        if vis[i] or i in dq:
            continue
        dq.append(i)
print(answer)