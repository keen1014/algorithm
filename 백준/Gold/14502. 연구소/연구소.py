def bfs(li):
    dq=deque(copy.deepcopy(virus))
    cnt=0
    bd=copy.deepcopy(board)
    for n in range(3):
        bd[li[n][0]][li[n][1]]=1
    while dq:
        for _ in range(len(dq)):
            v=dq.popleft()
            for i in range(4):
                y=v[0]+dy[i]
                x=v[1]+dx[i]
                if y<0 or x<0 or N<=y or M<=x or bd[y][x]==1 or bd[y][x]==2:
                    continue
                bd[y][x]=2
                dq.append([y,x])
    for i in range(N):
        for j in range(M):
            if bd[i][j]==0:
                cnt+=1
    # print(*bd, sep='\n', end='\n\n')
    answer.append(cnt)
def backtracking(z,n):
    if n==3:
        bfs(li)
        return
    for i in range(z,N*M):
        y=i//M
        x=i%M
        if board[y][x]==0:
            li[n]=[y,x]
            backtracking(i+1,n+1)
import sys
from collections import deque
import copy
input=sys.stdin.readline
N, M = map(int, input().strip().split())
virus=deque([])
dy=[-1,0,1,0]
dx=[0,1,0,-1]
answer=[]
li=[0,0,0]
board=[list(map(int, input().strip().split())) for i in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            virus.append([i,j])
backtracking(0,0)
print(max(answer))