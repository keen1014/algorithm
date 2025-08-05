import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
board=[[0 for _ in range(N)] for _ in range(N)]
K=int(input().strip())
apple=[tuple(map(int, input().strip().split()))for i in range(K)]
L=int(input().strip())
turn=deque([list(input().strip().split()) for i in range(L)])
for i in range(L):
    turn[i][0]=int(turn[i][0])
dx=[0,1,0,-1]
dy=[-1,0,1,0]
cnt=0
head=[0,0,1]
dq=deque([[0,0]])
while(1):
    if turn and turn[0][0]==cnt:
        if turn[0][1]=='L':
            head[2]=(head[2]+3)%4
        elif turn[0][1]=='D':
            head[2]=(head[2]+1)%4
        turn.popleft()
    cnt+=1
    y=head[0]+dy[head[2]]
    x=head[1]+dx[head[2]]
    if y<0 or x<0 or N<=y or N<=x or [y,x] in dq:
        print(cnt)
        exit()
    if (y+1,x+1) in apple:
        apple.remove((y+1,x+1))
    else:
        dq.pop()
    dq.appendleft([y,x])
    head[0]=y
    head[1]=x