import sys
from collections import deque
input= sys.stdin.readline
n, m=list(map(int, input().strip().split()))
nm=[]
for _ in range(m):
    nm.append(list(map(int, input().strip().split())))
dq=deque([])
mx=1
dx=[0,-1, 0, 1]
dy=[-1, 0, 1, 0]
for i in range(m):
    for j in range(n):
        if nm[i][j] == 1:
            dq.append([i, j])
while dq:
    tmp=dq.popleft()
    for z in range(4):
        x=dx[z]+tmp[0]
        y=dy[z]+tmp[1]
        if x<0 or y<0 or x>=m or y>=n:
            continue
        elif nm[x][y]==0:
            dq.append([x, y])
            nm[x][y]=nm[tmp[0]][tmp[1]]+1
            mx=max(nm[x][y], mx)
for d in nm:
    if 0 in d:
        print(-1)
        break
else:
    print(mx-1)
