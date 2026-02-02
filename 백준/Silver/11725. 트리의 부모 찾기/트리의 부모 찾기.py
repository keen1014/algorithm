import sys
from collections import defaultdict
from collections import deque
input=sys.stdin.readline
dic=defaultdict(deque)
N=int(input())
dq=deque([1])
vis=[False]*(N+1)
root=[0]*(N+1)
vis[0]=True
for _ in range(N-1):
    r, c = map(int, input().split())
    dic[r].append(c)
    dic[c].append(r)
while dq:
    temp=dq.popleft()
    if vis[temp]:
        continue
    vis[temp]=True
    while dic[temp]:
        z=dic[temp].popleft()
        if vis[z]:
            continue
        root[z]=temp
        dq.append(z)
for i in range(2, N+1):
    print(root[i])