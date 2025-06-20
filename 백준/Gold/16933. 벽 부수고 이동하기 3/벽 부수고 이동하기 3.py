import sys
from collections import deque
input=sys.stdin.readline
N, M, K=map(int, input().strip().split())
board=[list(map(int, input().strip()))for i in range(N)]
vis=[[[0 for i in range(M)] for j in range(N)] for k in range(K+1)]
time=False #아침, 밤
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
dq=deque([[K,0,0]])
vis[K][0][0]=1
time=False
while dq:
    T=1 #밤일때 기다리기 한번만하기 위한 조건 1참, 2 거짓, 3마지막에 올려야 하는가?
    tmp=dq.popleft()
    if [tmp[1],tmp[2]]==[N-1, M-1]:
                print(vis[tmp[0]][tmp[1]][tmp[2]])
                exit()
    if (vis[tmp[0]][tmp[1]][tmp[2]]+1)%2==0:
        time=True
    else:
        time=False
    for i in range(4):
        x=dx[i]+tmp[2]
        y=dy[i]+tmp[1]
        if x<0 or y<0 or x>=M or y>=N or vis[tmp[0]][y][x]!=0 or \
            (tmp[0]<K and vis[tmp[0]+1][y][x]!=0) or (tmp[0]==0 and board[y][x]==1):
            continue
        if board[y][x]==0:
            vis[tmp[0]][y][x]=vis[tmp[0]][tmp[1]][tmp[2]]+1
            dq.append([tmp[0], y, x])
            if [y,x]==[N-1, M-1]:
                print(vis[tmp[0]][y][x])
                exit()
        if board[y][x]==1 and tmp[0]>0 and time==True and vis[tmp[0]-1][y][x]==0:
            vis[tmp[0]-1][y][x]=vis[tmp[0]][tmp[1]][tmp[2]]+1
            dq.append([tmp[0]-1, y, x])
        elif board[y][x]==1 and tmp[0]>0 and time==False and vis[tmp[0]-1][y][x]==0 and T==1: #한번만 해야함 지금은 2개 있으면 2번 3개면 3번
            dq.append([tmp[0], tmp[1], tmp[2]])
            T=3
    else:
        if T==3:
            vis[tmp[0]][tmp[1]][tmp[2]]=vis[tmp[0]][tmp[1]][tmp[2]]+1
else:
    print(-1)