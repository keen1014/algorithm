import sys
from collections import deque
input=sys.stdin.readline
N, K = map(int, input().split())

dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]
board=[]
dic={}
for i in range(1, K+1):
    dic[i]=deque()
for _ in range(N):
    board.append(list(map(int, input().split())))

S, ay, ax = map(int, input().split())

dq=deque([])
for i in range(N):
    for j in range(N):
        if board[i][j]:
            dic[board[i][j]].append([i, j])

for i in range(S):
    for j in range(1, K+1):
        newdic=deque()
        while dic[j]:
            iy, ix=dic[j].popleft()
            for z in range(4):
                x=dx[z]+ix
                y=dy[z]+iy
                if x<0 or y<0 or N<=x or N<=y or board[y][x]:
                    continue
                board[y][x]=j
                newdic.append([y,x])
        dic[j]=newdic
print(board[ay-1][ax-1])