import sys
from collections import deque
input=sys.stdin.readline
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
N, M=map(int, input().strip().split())
board=[list(map(int, input().strip()))for _ in range(N)]
dq=deque([])
wdq=[]
vis=[[[0 for s in range(M)]for _ in range(N)]for q in range(2)]
vis[1][0][0]=1
vis[0][0][0]=1
dq.append([1, 0, 0])
while dq:
    tmp=dq.popleft()
    for v in range(4):
        y=dy[v]+tmp[1]
        x=dx[v]+tmp[2]
        if x<0 or y<0 or x>=M or y>=N or (board[y][x]==1 and tmp[0]==0) or vis[tmp[0]][y][x]!=0:
            continue
        else:
            if board[y][x]==1:
                dq.append([tmp[0]-1, y, x])
                vis[tmp[0]-1][y][x]=vis[tmp[0]][tmp[1]][tmp[2]]+1
            else:
                dq.append([tmp[0], y, x])
                vis[tmp[0]][y][x]=vis[tmp[0]][tmp[1]][tmp[2]]+1
if vis[0][N-1][M-1]==0 and vis[1][N-1][M-1]==0:
    print(-1)
elif vis[0][N-1][M-1]==0:
    print(vis[1][N-1][M-1])
elif vis[1][N-1][M-1]==0:
    print(vis[0][N-1][M-1])
else:
    print(min(vis[0][N-1][M-1], vis[1][N-1][M-1]))