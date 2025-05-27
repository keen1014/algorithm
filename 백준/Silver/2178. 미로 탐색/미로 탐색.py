import sys
from collections import deque
input= sys.stdin.readline
n, m=map(int, input().strip().split())
nm=[]
dq=deque([])
vis = [[0 for _ in range(m)] for i in range(n)]
for i in range(n):
    tmp=[]
    for j in input().strip():
        tmp.append(j)
    nm.append(tmp)
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]
for i in range(n):
    for j in range(m):
        if i ==0 and j == 0:
            dq.append([0, 0])
            vis[0][0]=1
        while dq:
            tmp=dq.popleft()
            for z in range(4):
                x=tmp[0]+dx[z]
                y=tmp[1]+dy[z]
                if x<0 or y<0 or x>=n or y>=m:
                    continue
                elif nm[x][y]=='1':
                    dq.append([x, y])
                    nm[x][y]=0
                    vis[x][y]=vis[tmp[0]][tmp[1]]+1
                    
print(vis[n-1][m-1])