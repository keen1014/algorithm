import sys
from collections import deque
input=sys.stdin.readline
dq=deque([])
dq0=deque([])
N, K=map(int, input().strip().split())
board=[-1 for i in range(100001)]
cnt=0
dx=[-1, 1]
dq.append([N, cnt])
board[N]=cnt
while dq:
    if board[K]!=-1:
        print(board[K])
        break
    tmp=dq.popleft()
    if tmp[0]<K and 0<tmp[0]:
        tmp2=tmp[0]*2
        if tmp2<=100000 and board[tmp2]==-1:
            board[tmp2]=tmp[1]
            dq.appendleft([tmp2, tmp[1]])
    for i in range(2):
        x=tmp[0]+dx[i]
        if 0 <= x <= 100000 and board[x]==-1:
            board[x]=tmp[1]+1
            dq.append([x,tmp[1]+1])