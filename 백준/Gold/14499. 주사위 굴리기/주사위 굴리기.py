import sys
from collections import deque
input=sys.stdin.readline
N,M,y,x,K=map(int, input().strip().split())
dice=[[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
board=[list(map(int, input().strip().split())) for i in range(N)]
li=deque(list(map(int,input().strip().split())))
for i in range(K):
    tmp=li.popleft()-1
    if x+dx[tmp]<0 or y+dy[tmp]<0 or M<=x+dx[tmp] or N<=y+dy[tmp]:
        continue
    x+=dx[tmp]
    y+=dy[tmp]
    if tmp==0:
        temp=dice[1][0]
        dice[1][0]=dice[1][1]
        dice[1][1]=dice[1][2]
        dice[1][2]=dice[3][1]
        dice[3][1]=temp
    elif tmp==1:
        temp=dice[1][2]
        dice[1][2]=dice[1][1]
        dice[1][1]=dice[1][0]
        dice[1][0]=dice[3][1]
        dice[3][1]=temp
    elif tmp==2:
        temp=dice[3][1]
        dice[3][1]=dice[2][1]
        dice[2][1]=dice[1][1]
        dice[1][1]=dice[0][1]
        dice[0][1]=temp
    elif tmp==3:
        temp=dice[0][1]
        dice[0][1]=dice[1][1]
        dice[1][1]=dice[2][1]
        dice[2][1]=dice[3][1]
        dice[3][1]=temp
    if board[y][x]==0:
        board[y][x]=dice[1][1]
    else:
        dice[1][1]=board[y][x]
        board[y][x]=0
    print(dice[3][1])