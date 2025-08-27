def backtracking(n,s):
    if n==M:
        vis=[[-1 for i in range(N)] for j in range(N)]
        # print(svli)
        for z in svli:
            dq.append(z)
            vis[z[0]][z[1]]=0
        # print(dq)
        BFS(vis)
        return
    for i in range(s, len(virusli)):
        svli[n]=virusli[i]
        backtracking(n+1,i+1)
def BFS(vis):
    while dq:
        tmp=dq.popleft()
        for i in range(4):
            x=dx[i]+tmp[1]
            y=dy[i]+tmp[0]
            if y<0 or x<0 or N<=y or N<=x or vis[y][x]!=-1:
                continue
            if board[y][x]==1:
                vis[y][x]=-2
                continue
            dq.append([y,x])
            vis[y][x]=vis[tmp[0]][tmp[1]]+1
    m=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                vis[i][j]=-2
            if vis[i][j]==-1:
                return
            if m< vis[i][j]:
                m=vis[i][j]
    # print(*vis, sep='\n')
    answer.append(m)
            
import sys
from collections import deque
input=sys.stdin.readline
N, M=list(map(int, input().strip().split()))
board=[list(map(int, input().strip().split())) for _ in range(N)]
dq=deque([])
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
answer=[]
virusli=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==2:
            virusli.append([i,j])
# print(virusli)
svli=[[0,0] for _ in range(M)]

backtracking(0,0)
if answer==[]:
    print(-1)
else:
    # print(answer)
    print(min(answer))