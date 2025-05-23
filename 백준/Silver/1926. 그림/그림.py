import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]
board=[]
dq=deque([])
vis=[[0 for _ in range(m)] for w in range(n)]
total=[]
for i in range(n):
    board.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and vis[i][j]!=1:
            dq.append([i,j])
            vis[i][j]=1
            cnt=0
            while dq:
                cnt+=1
                tmp=dq.popleft()
                for k in range(4):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or y<0 or x>=n or y>=m:
                        continue
                    elif board[x][y]==0 or vis[x][y]==1:
                        continue
                    dq.append([x,y])
                    vis[x][y]=1
            else:
                total.append(cnt)
if total:
    print(len(total))
    print(max(total))
else:
    print(0)
    print(0)
    