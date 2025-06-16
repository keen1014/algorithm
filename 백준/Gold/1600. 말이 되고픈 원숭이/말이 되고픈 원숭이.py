import sys
from collections import deque
input=sys.stdin.readline
K=int(input().strip())
W, H=map(int, input().strip().split())
board=[list(map(int, input().strip().split())) for i in range(H)]
monkey_vis=[[[0 for i in range(W)] for j in range(H)] for _ in range(K+1)]
dx_horse=[-1, -2, -2, -1, 1, 2, 2, 1]
dy_horse=[-2, -1, 1, 2, 2, 1, -1, -2]
dx_monkey=[0, -1, 0, 1]
dy_monkey=[-1, 0, 1, 0]
dq=deque([])
dq.append([0,0,K,0])
monkey_vis[K][0][0]=1
while dq:
    tmp=dq.popleft()
    if [tmp[0], tmp[1]]==[H-1, W-1]:
        print(tmp[3])
        break
    for i in range(4):
        x=dx_monkey[i]+tmp[1]
        y=dy_monkey[i]+tmp[0]
        if x<0 or y<0 or x>=W or y>=H or board[y][x]==1 or monkey_vis[tmp[2]][y][x]:
            continue
        dq.append([y, x, tmp[2], tmp[3]+1])
        monkey_vis[tmp[2]][y][x]=1
    if tmp[2]!=0:
        for i in range(8):
            x=dx_horse[i]+tmp[1]
            y=dy_horse[i]+tmp[0]
            if x<0 or y<0 or x>=W or y>=H or board[y][x]==1 or monkey_vis[tmp[2]-1][y][x]:
                continue
            dq.append([y, x, tmp[2]-1, tmp[3]+1])
            monkey_vis[tmp[2]-1][y][x]=1
else:
    print(-1)