import sys
from collections import deque
input=sys.stdin.readline
M, N, K=map(int, input().strip().split())
board=[[0 for i in range(N)]for j in range(M)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
dq=deque([])
stack=[]
for _ in range(K):
    lx, ly, rx, ry= map(int, input().strip().split())
    for i in range(ry-ly):
        for j in range(rx-lx):
            board[ly+i][lx+j]=1


for i in range(M):
    for j in range(N):
        cnt=0
        if board[i][j]==0:
            dq.append([i, j])
            while dq:
                tmp=dq.popleft()
                board[tmp[0]][tmp[1]]=8
                cnt+=1
                for k in range(4):
                    x=dx[k]+tmp[1]
                    y=dy[k]+tmp[0]
                    if x<0 or y<0 or x>=N or y>=M or board[y][x]==1 or board[y][x]==8:
                        continue
                    else:
                        board[y][x]=8
                        dq.append([y, x])
                        
            stack.append(cnt)
print(len(stack))
print(*sorted(stack))

                        