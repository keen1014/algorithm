import sys
from collections import deque
input=sys.stdin.readline
N, M, K=map(int, input().strip().split())
board=[list(map(int, input().strip()))for i in range(N)]
vis=[[[0 for i in range(M)] for j in range(N)]for k in range(K+1)]
dx=[0,-1,0,1]
dy=[-1,0,1,0]
dq=deque([])
dq.append([0,0,K]) #y, x, 남은 벽
vis[K][0][0]=1
while dq:
    tmp=dq.popleft()
    for i in range(4):
        x=dx[i]+tmp[1]
        y=dy[i]+tmp[0]
        if x<0 or y<0 or x>=M or y>=N or vis[tmp[2]][y][x]!=0 or (board[tmp[0]][tmp[1]]==1 and vis[tmp[2]+1][y][x]!=0) or (board[tmp[0]][tmp[1]]==1 and vis[tmp[2]+1][y][x]==1):
            continue
        elif board[y][x]==0 and vis[tmp[2]][y][x]==0:
            if vis[tmp[2]][y][x]!=0 and vis[tmp[2]][y][x]<=vis[tmp[2]][tmp[0]][tmp[1]]+1:
                continue
            vis[tmp[2]][y][x]=vis[tmp[2]][tmp[0]][tmp[1]]+1
            dq.append([y, x, tmp[2]])
            if [y, x]==[N-1, M-1]:
                print(vis[tmp[2]][y][x])
                exit()
        if board[y][x]==1 and tmp[2]!=0:
            if vis[tmp[2]-1][y][x]!=0 and vis[tmp[2]][y][x]<=vis[tmp[2]][tmp[0]][tmp[1]]+1:
                continue
            vis[tmp[2]-1][y][x]=vis[tmp[2]][tmp[0]][tmp[1]]+1
            dq.append([y, x, tmp[2]-1])
            if [y, x]==[N-1, M-1]:
                print(vis[tmp[2]][y][x])
                exit()
else:
    if vis[K][N-1][M-1]!=0:
        print(vis[K][N-1][M-1])
    else:
        print(-1)