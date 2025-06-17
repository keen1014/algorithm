import sys
from collections import deque
input=sys.stdin.readline
N, K= map(int, input().strip().split())
board=[-1 for i in range(100001)]
dq=deque([])
dx=[-1,1]
dq.append(N)
board[N]=-2
stack=[]
cnt=0
while dq:
    if board[K]!=-1:
        break
    tmp=dq.popleft()
    for i in range(2):
        x=dx[i]+tmp
        if x<0 or x>100000 or board[x]!=-1:
            continue
        board[x]=tmp
        dq.append(x)
        if board[K]!=-1:
            break
    if board[K]!=-1:
        break
    if tmp<K:
        x=tmp*2
        if x<0 or x>100000 or board[x]!=-1:
            continue
        board[x]=tmp
        dq.append(x)
tmp=board[K]
stack.append(K)
while tmp!=-2:
    cnt+=1
    stack.append(tmp)
    tmp=board[tmp]
print(cnt)
print(*stack[::-1])