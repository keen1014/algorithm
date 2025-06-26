import sys
from collections import deque
input=sys.stdin.readline
N, M=map(int, input().strip().split())
board=[[0 for i in range(N)]for j in range(N)]
vis=[[0 for i in range(N)]for j in range(N)]
switch=[[[] for i in range(N)]for j in range(N)]
light=[[0 for i in range(N)]for j in range(N)]
dq=deque([[0,0]])
dx=[0,-1,0,1]
dy=[-1,0,1,0]
cnt=1
for i in range(M):
    x,y,a,b=list(map(int, input().strip().split()))
    switch[x-1][y-1].append([a-1,b-1])
vis[0][0]=1
light[0][0]=1
while dq:
    tmp=dq.popleft()
    while switch[tmp[0]][tmp[1]]:
        t=switch[tmp[0]][tmp[1]].pop()
        if light[t[0]][t[1]]==0:
            light[t[0]][t[1]]=1
            cnt+=1
        for i in range(4):
            y=t[0]+dy[i]
            x=t[1]+dx[i]
            if 0>x or 0>y or x>=N or y>=N or vis[y][x]==0:
                continue
            dq.append([t[0],t[1]])
            vis[t[0]][t[1]]=1
            break
    for i in range(4):
        y=tmp[0]+dy[i]
        x=tmp[1]+dx[i]
        if 0>x or 0>y or x>=N or y>=N or vis[y][x]==1 or light[y][x]==0:
            continue
        dq.append([y,x])
        vis[y][x]=1

print(cnt)