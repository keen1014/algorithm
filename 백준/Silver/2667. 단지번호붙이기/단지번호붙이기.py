import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
dq=deque([])
stack=[]
cnt=0
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
board=[list(map(int, input().strip()))for j in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            dq.append([i, j])
            while dq:
                tmp=dq.popleft()
                cnt+=1
                board[tmp[0]][tmp[1]]=-1
                for k in range(4):
                    x=dx[k]+tmp[1]
                    y=dy[k]+tmp[0]
                    if x<0 or y<0 or x>=N or y>=N or board[y][x]!=1:
                        continue
                    else:
                        dq.append([y, x])
                        board[y][x]=-1
            stack.append(cnt)
            cnt=0
            
print(len(stack))
print(*sorted(stack), sep='\n')