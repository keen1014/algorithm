def clean(y,x,d):
    global cnt
    if vis[y][x]==False:
        vis[y][x]=True
        cnt+=1
import sys
input=sys.stdin.readline
N,M=map(int,input().strip().split())
y,x,d=map(int,input().strip().split())
board=[list(map(int, input().strip().split()))for i in range(N)]
vis=[[False for i in range(M)] for j in range(N)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
cnt=0
while(1):
    clean(y,x,d)
    for _ in range(4):
        d=(d+3)%4
        lx=x+dx[d]
        ly=y+dy[d]
        if lx<0 or ly<0 or M<lx or N<ly or board[ly][lx]==1 or vis[ly][lx]==True:
            continue
        x=lx
        y=ly
        clean(y,x,d)
        break
    else:
        lx=x+dx[(d+2)%4]
        ly=y+dy[(d+2)%4]
        if board[ly][lx]==1:
            print(cnt)
            exit()
        x=lx
        y=ly