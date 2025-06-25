import sys
from collections import deque
input=sys.stdin.readline
N, M, P=map(int, input().strip().split())
move=list(map(int, input().strip().split()))
board=[list(input().strip())for i in range(N)]
vis=[[0 for i in range(M)]for j in range(N)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
cnt=[0 for i in range(P)]
dq=[deque([]) for i in range(P)]
c=1
for i in range(N):
    for j in range(M):
        if board[i][j]!='.' and board[i][j]!='#':
            cnt[int(board[i][j])-1]+=1
            vis[i][j]=int(board[i][j])
            dq[int(board[i][j])-1].append([i, j])
while c:
    c=0
    for i in range(P):
        for k in range(move[i]):
            if dq[i]:
                for j in range(len(dq[i])):
                    tmp=dq[i].popleft()
                    for z in range(4):
                        x=dx[z]+tmp[1]
                        y=dy[z]+tmp[0]
                        if x<0 or y<0 or x>=M or y>=N or board[y][x]!='.' or vis[y][x]!=0:
                            continue
                        vis[y][x]=vis[tmp[0]][tmp[1]]
                        dq[i].append([y, x])
                        cnt[i]+=1
                        c+=1 
            else:
                break
print(*cnt)