def BFS():
    global T
    while T:
        boardtmp=[[0 for i in range(C)] for j in range(R)]
        for li in range(R):
            for lj in range(C):
                if board[li][lj]<0:
                    continue
                z=board[li][lj]//5
                re=0
                for ii in range(4):
                    y=li+dy[ii]
                    x=lj+dx[ii]
                    if y<0 or x<0 or R<=y or C<=x or board[y][x]==-1:
                        continue
                    re+=1
                    boardtmp[y][x]+=z
                board[li][lj]-=re*z
        for i in range(R):
            for j in range(C):
                board[i][j]+=boardtmp[i][j]
        # print(*board, sep='\n', end='\n\n')
        ### 공기청정기 작동 코드작성
        
        airtmp=airgun[0]
        y,x=airtmp[0]-1,airtmp[1]
        while 0<y:
            board[y][x]=board[y-1][x]
            y-=1
        while x<C-1:
            board[y][x]=board[y][x+1]
            x+=1
        while y<airtmp[0]:
            board[y][x]=board[y+1][x]
            y+=1
        while airtmp[1]+1<x:
            board[y][x]=board[y][x-1]
            x-=1
        board[y][airtmp[1]+1]=0

        
        airtmp=airgun[1]
        y,x=airtmp[0]+1,airtmp[1]
        while y<R-1:
            board[y][x]=board[y+1][x]
            y+=1
        while x<C-1:
            board[y][x]=board[y][x+1]
            x+=1
        while airtmp[0]<y:
            board[y][x]=board[y-1][x]
            y-=1
        while airtmp[1]+1<x:
            board[y][x]=board[y][x-1]
            x-=1
        board[y][airtmp[1]+1]=0
        T-=1
        # print(*board, sep='\n', end='\n\n')

        
import sys
from collections import deque
import copy
input=sys.stdin.readline
dx=[0,1,0,-1]
dy=[-1,0,1,0]
dq=deque([])
R, C, T=list(map(int, input().strip().split()))
board=[list(map(int, input().strip().split())) for _ in range(R)]
airgun=[]
answer=0
for i in range(R):
    for j in range(C):
        if board[i][j]==-1:
            airgun.append([i,j])
# print(*board, sep='\n')
BFS()
for k in range(R):
    for z in range(C):
        if board[k][z]!=0 and board[k][z]!=-1:
            answer+=board[k][z]
print(answer)