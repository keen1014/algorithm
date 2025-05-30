import sys
from collections import deque
input=sys.stdin.readline
dq=deque([])
dx=[0, -1, 0, 1, 0, 0]
dy=[-1, 0, 1, 0, 0, 0]
dz=[0, 0, 0, 0, 1, -1]
answer=0
n, m, h = map(int, input().strip().split())
tomato=[[[int(i) for i in input().strip().split()]for j in range(m)]for k in range(h)]
for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k]==1:
                dq.append([i, j, k])
while dq:
    tmp=dq.popleft()
    for i in range(6):
        x=dx[i]+tmp[2]
        y=dy[i]+tmp[1]
        z=dz[i]+tmp[0]
        if x<0 or y<0 or z<0 or x>=n or y>=m or z>=h or tomato[z][y][x]!=0:
            continue    
        else:
            if tomato[z][y][x]==0:
                tomato[z][y][x]=tomato[tmp[0]][tmp[1]][tmp[2]]+1
                dq.append([z, y, x])
for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k]==0:
                answer=-1
            elif answer!=-1 and answer<tomato[i][j][k]:
                answer=tomato[i][j][k]-1
print(answer)
                