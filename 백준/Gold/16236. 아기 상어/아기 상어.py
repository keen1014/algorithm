def BFS(n):
    global eat, answer
    while dq:
        li=[]
        for _ in range(len(dq)):
            tmp=dq.popleft()
            for i in range(4):
                y=tmp[0]+dy[i]
                x=tmp[1]+dx[i]
                if y<0 or x<0 or N<=y or N<=x or vis[y][x]!=-1 or n<board[y][x]:
                    continue
                vis[y][x]=vis[tmp[0]][tmp[1]]+1
                if board[y][x]==n or board[y][x]==0:
                    dq.append([y,x])
                elif board[y][x]!=0 and board[y][x]<n:
                    li.append([vis[y][x],y,x]) #거리, y, x
        if li!=[]:
            li=sorted(li)
            # print(li)
            # print(eat, n)
            eat+=1
            if eat==n:
                eat=0
                n+=1
            while dq:
                dq.popleft()
            dq.append([li[0][1],li[0][2]])
            board[li[0][1]][li[0][2]]=0
            answer+=li[0][0]
            # print(answer)
            for i in range(N):
                for j in range(N):
                    vis[i][j]=-1
            vis[li[0][1]][li[0][2]]=0
            


import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
board=[list(map(int, input().strip().split())) for _ in range(N)]
vis=[[-1 for i in range(N)]for j in range(N)]
dq=deque([])
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
ssize=2
eat=0
answer=0
# print(*board, sep='\n')
for i in range(N):
    for j in range(N):
        if board[i][j]==9:
            dq.append([i,j])
            board[i][j]=0
            vis[i][j]=0

BFS(ssize)
print(answer)