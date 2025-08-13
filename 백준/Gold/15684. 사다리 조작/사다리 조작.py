def asdf(k):
    for j in range(N):
        x=j
        for i in range(M):
            if board[i][x][1]:
                while board[i][x][1]==1:
                    x+=1
            elif board[i][x][0]:
                while board[i][x][0]==1:
                    x-=1
        # print(j+1,":", x+1)
        if j+1==x+1:
            li[j]=True
        else:
            li[j]=False
    if False not in li:
        print(k)
        exit()
    
def backtracking(n, s, k):
    if n==k:
        # print(nli)
        asdf(k)
        return
    for i in range(s, M*N):
        y=i//N
        x=i%N
        if N-2<x or board[y][x][1]!=0 or board[y][x][0]!=0 or board[y][x+1][1]!=0:
            continue
        board[y][x][1]=1
        board[y][x+1][0]=1
        nli.append([y,x])
        backtracking(n+1, i+1, k)
        nli.pop()
        board[y][x][1]=0
        board[y][x+1][0]=0
        

import sys
from collections import deque
input=sys.stdin.readline
N, H, M = map(int, input().strip().split())
board=[[[0, 0] for i in range(N)] for j in range(M)]
wline=[]
li=[False]*N
nli=[]
for i in range(H):
    h, w=map(int, input().strip().split())
    board[h-1][w-1]=[0,1]
    board[h-1][w]=[1,0]
    wline.append([h-1,w-1])
# print('wline',wline)
# print(*board, sep='\n')
backtracking(0,0,0)
backtracking(0,0,1)
backtracking(0,0,2)
backtracking(0,0,3)
print(-1)