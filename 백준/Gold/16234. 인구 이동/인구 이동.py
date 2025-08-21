def BFS():
    ans=0
    lie=[]
    lie.append(dq[0])
    vis[dq[0][0]][dq[0][1]]=True
    while dq:
        tmp=dq.popleft()
        ans+=board[tmp[0]][tmp[1]]
        for i in range(4):
            y=dy[i]+tmp[0]
            x=dx[i]+tmp[1]
            if y<0 or x<0 or N<=y or N<=x or vis[y][x]==True or abs(board[tmp[0]][tmp[1]]-board[y][x])<L or R<abs(board[tmp[0]][tmp[1]]-board[y][x]):
                continue
            dq.append([y,x])
            lie.append([y,x])
            vis[y][x]=True
    federation.append(ans)
    return lie
    
        
import sys
from collections import deque
input=sys.stdin.readline
N, L, R= list(map(int, input().strip().split()))
board=[list(map(int, input().strip().split())) for _ in range(N)]
dq=deque([])
federation=[]
cnt=0
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
while True:
    federation=[]
    vis=[[False] * N for _ in range(N)]
    li=[]
    for i in range(N):
        for j in range(N):
            if vis[i][j]==True:
                continue
            dq.append([i,j])
            li.append(BFS())
    if len(li) == N*N:
        print(cnt)
        break
    cnt+=1
    for i in range(len(li)):
        d=federation[i]//len(li[i])
        while li[i]:
            tmp=li[i].pop()
            board[tmp[0]][tmp[1]]=d