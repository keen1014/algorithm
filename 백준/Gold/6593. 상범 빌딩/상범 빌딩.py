import sys
from collections import deque
input=sys.stdin.readline
dx=[0, -1, 0, 1, 0, 0]
dy=[-1, 0, 1, 0, 0, 0]
dz=[0, 0, 0, 0, 1, -1]
dq=deque([])
while True:
    L, R, C = map(int, input().strip().split())
    if L == 0 and R == 0 and C == 0:
        break
    board=[]
    for x in range(L):
        tmp=[]
        for _ in range(R):
            tmp.append(list(input().strip()))
        input()
        board.append(tmp)
    vis=[]
    for x in range(L):
        tmp=[]
        for _ in range(R):
            tmp.append([0 for k in range(C)])
        vis.append(tmp)
    E=[]
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k]=='E':
                    E=[i, j, k]
                if board[i][j][k]=='S':
                    dq.append([i, j, k])
                    vis[i][j][k]=1
                while dq:
                    temp=dq.popleft()
                    for n in range(6):
                        x=dx[n]+temp[2]
                        y=dy[n]+temp[1]
                        z=dz[n]+temp[0]
                        if x<0 or y<0 or z<0 or x>=C or y>=R or z>=L or board[z][y][x]=='#' or vis[z][y][x]!=0:
                            continue
                        else:
                            dq.append([z, y, x])
                            vis[z][y][x]=vis[temp[0]][temp[1]][temp[2]]+1
    else:
        if vis[E[0]][E[1]][E[2]]==0:
            print('Trapped!')
        else:
            print(f'Escaped in {vis[E[0]][E[1]][E[2]]-1} minute(s).')