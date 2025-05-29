import sys
from collections import deque
input=sys.stdin.readline
T= int(input().strip())
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
for _ in range(T):
    cnt=0
    n, m, k=map(int, input().strip().split())
    board=[[0 for i in range(n)]for j in range(m)]
    dq=deque([])
    for i in range(k):
        visx, visy=map(int, input().strip().split())
        board[visy][visx]=1
    for i in range(m):
        for j in range(n):
            if board[i][j]==1:
                dq.append([i, j])
                board[i][j]=-1
                cnt+=1
            while dq:
                tmp=dq.popleft()
                for ewsn in range(4):
                    x=dx[ewsn]+tmp[1]
                    y=dy[ewsn]+tmp[0]
                    if x<0 or y<0 or x>=n or y>=m or board[y][x]==0 or board[y][x]==-1:
                        continue
                    else:
                        dq.append([y, x])
                        board[y][x]=-1
    print(cnt)