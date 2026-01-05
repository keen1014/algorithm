import sys
from collections import deque
input=sys.stdin.readline
N, K, M= map(int, input().split())
# print(N, K, M)
matrix=[]

adj=[[] for _ in range(N+1)]

for i in range(M):
    li=list(map(int, input().split()))
    matrix.append(li)
    for z in li:
        adj[z].append(i)

dq= deque([(1,0)])
vis=[False]*(N+1)
vis_tube=[False]*M
while dq:
    tmp=dq.popleft()
    if tmp[0]==N:
        print(tmp[1]+1)
        break
    
    for id in adj[tmp[0]]:
        if vis_tube[id]:
            continue
        vis_tube[id]=True
        
        for x in matrix[id]:
            if vis[x]:
                continue
            vis[x]=True
            dq.append((x, tmp[1]+1))
else:
    print(-1)