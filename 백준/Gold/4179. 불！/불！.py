import sys
from collections import deque
input= sys.stdin.readline
n, m=list(map(int, input().strip().split()))
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
board= []
dq=deque([])
fdq=deque([])
jdq=deque([])
fire=[[0 for i in range(m)]for j in range(n)]
jihun=[[0 for i in range(m)]for j in range(n)]
for i in range(n):
    tmp=input().strip()
    board.append(list(tmp))
for i in range(n):
    for j in range(m):
        if board[i][j]=='J':
            jdq.append([i, j])
            dq.append([i, j])
            board[i][j]=1
            jihun[i][j]=1
        elif board[i][j]=='F':
            fdq.append([i, j])
            board[i][j]=1
            fire[i][j]=1
while fdq:
    tmp= fdq.popleft()
    for i in range(4):
        x=dx[i]+tmp[0]
        y=dy[i]+tmp[1]
        if x<0 or y<0 or x>=n or y >= m or board[x][y]=='#':
            continue
        elif fire[x][y]==0:
            fire[x][y]=fire[tmp[0]][tmp[1]]+1
            fdq.append([x, y])
while jdq:
    tmp= jdq.popleft()
    if tmp[0]==n-1 or tmp[1]==m-1 or tmp[0]==0 or tmp[1]==0:
        print(jihun[tmp[0]][tmp[1]])
        break
    for i in range(4):
        x=dx[i]+tmp[0]
        y=dy[i]+tmp[1]
        if x<0 or y<0 or x>=n or y >= m or board[x][y]=='#':
            continue
        elif jihun[x][y]==0 and (jihun[tmp[0]][tmp[1]]+1<fire[x][y] or fire[x][y] == 0):
            jihun[x][y]=jihun[tmp[0]][tmp[1]]+1
            jdq.append([x, y])
else:
    print('IMPOSSIBLE')