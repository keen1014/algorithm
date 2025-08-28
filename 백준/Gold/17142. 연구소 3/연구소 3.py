def backtracking(n,k):
    if n==M:
        vis=[[-1 for z in range(N)] for s in range(N)]
        # print(*vis, sep='\n')
        # print(vli)
        for v in vli:
            dq.append(v)
            vis[v[0]][v[1]]=0
        # print(dq)
        BFS(vis)
        # print(*vis,sep='\n')
        return
    for i in range(k, len(virus)):
        vli[n]=virus[i]
        backtracking(n+1, i+1)
def BFS(vis):
    while dq:
        tmp=dq.popleft()
        for i in range(4):
            x=dx[i]+tmp[1]
            y=dy[i]+tmp[0]
            if y<0 or x<0 or N<=y or N<=x or vis[y][x]!=-1 or board[y][x]==1:
                continue
            vis[y][x]=vis[tmp[0]][tmp[1]]+1
            dq.append([y,x])
            
    m=0
    for iy in range(N):
        for ix in range(N):
            if board[iy][ix]==2:
                vis[iy][ix]=0
            if board[iy][ix]==1:
                vis[iy][ix]=-2
            if vis[iy][ix]==-1:
                return
            if m<vis[iy][ix]:
                m=vis[iy][ix]
    # print(m)
    answer.append(m)
    return
import sys
from collections import deque
input=sys.stdin.readline
N, M = list(map(int, input().strip().split()))
board=[list(map(int, input().strip().split())) for i in range(N)]
virus=[]
dq=deque([])
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
vli=[[0,0] for _ in range(M)]
answer=[]
# print(*board, sep='\n')
for i in range(N):
    for j in range(N):
        if board[i][j]==2:
            virus.append([i,j])
# print(virus)
backtracking(0,0)
if answer==[]:
    print(-1)
else:
    print(min(answer))