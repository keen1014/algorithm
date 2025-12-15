from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
N, M=map(int, input().split())
dic=defaultdict(list)
vis=[False]*(N+1)
li=[]*(N+1)
for i in range(M):
    u, v=map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)
answer=0
for j in range(1, N+1):
    if vis[j]:
        continue
    answer+=1
    dq=deque()
    dq.append(j)
    while dq:
        z=dq.pop()
        while dic[z]:
            tmp=dic[z].pop()
            if vis[tmp]:
                continue
            vis[tmp]=True
            dq.append(tmp)

print(answer)