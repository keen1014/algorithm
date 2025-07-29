def DFS():
    cnt=1
    li=[]
    vis=[[False]*6 for i in range(12)]
    li.append(dq[0])
    while dq:
        y,x=dq.pop()
        vis[y][x]=True
        for i in range(4):
            jy=y+dy[i]
            jx=x+dx[i]
            if jy<0 or jx<0 or 6<=jx or 12<=jy or board[jy][jx]!=board[y][x] or vis[jy][jx]:
                continue
            dq.append([jy, jx])
            li.append([jy, jx])
            vis[jy][jx]=True
            cnt+=1
    if 4<=cnt:
        while li:
            ly, lx=li.pop()
            board[ly][lx]='.'
        return cnt
    return 0


def sorrrt():
    for i in range(6):
        li=[]
        for j in range(12):
            if board[j][i]!='.':
                li.append(board[j][i])
        for k in range(11, -1, -1):
            if li:
                board[k][i]=li.pop()
            else:
                board[k][i]='.'
import sys
from collections import deque
input=sys.stdin.readline
board=[list(input().strip()) for i in range(12)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
dq=deque([])
re=True
cnt=0
while re:
    answer=0
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                dq.append([i,j])
                answer+=DFS()
    if 0==answer:
        re=False
    else:
        cnt+=1
        sorrrt()
print(cnt)