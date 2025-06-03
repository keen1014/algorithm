import sys
from collections import deque
input=sys.stdin.readline
dq=deque([])
N=int(input().strip())
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
stack=[]
m=[]
board=[list(map(int, input().strip().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        stack.append(board[i][j])
stack=set(stack)
for k in stack:
    cnt=0
    vis=[[0 for _ in range(N)]for w in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]>k and vis[i][j]==0:
                dq.append([i, j])
                vis[i][j]=1
                cnt+=1
                while dq:
                    tmp=dq.popleft()
                    for z in range(4):
                        x=dx[z]+tmp[1]
                        y=dy[z]+tmp[0]
                        if x<0 or y<0 or x>=N or y>=N or board[y][x]<=k or vis[y][x]==1:
                            continue
                        else:
                            dq.append([y, x])
                            vis[y][x]=1
    m.append(cnt)
if max(m) ==0:
    print(1)
else:
    print(max(m))