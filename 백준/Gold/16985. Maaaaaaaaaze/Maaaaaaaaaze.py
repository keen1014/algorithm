def rotation(list, n):
    if n == 0:
        return list
    rtboard=[[0 for i in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rtboard[j][5-1-i]=list[i][j]
    return rotation(rtboard, n-1)

def backtracking(jo, n):
    if n==5:
        # print(*li)
        b=[]
        for i in range(len(li)):
            b.append(rotationboard[jo[i]][li[i]])
        # print(*b[0], sep='\n')
        if b[4][4][4]==0:
            return
        visbfs=[[[0 for i in range(5)]for j in range(5)]for k in range(5)]
        dq.append([0,0,0])
        BFS(visbfs,b)
        if visbfs[4][4][4]!=0:
            answer.append(visbfs[4][4][4])
        # print(*visbfs, sep='\n')
        return
    for i in range(4):
        li[n]=i
        backtracking(jo, n+1)

def mixture(n):
    if n==5:
        # print(*johap)
        backtracking(johap, 0)
        # print('\n\n')
        return
    for i in range(5):
        if vis[i]==False:
            johap[n]=i
            vis[i]=True
            mixture(n+1)
            vis[i]=False

def BFS(visbfs, B):
    while dq:
        z,y,x=dq.popleft()
        if B[z][y][x]==1:
            for i in range(6):
                lz=z+dz[i]
                ly=y+dy[i]
                lx=x+dx[i]
                if lz<0 or ly<0 or lx<0 or 5<=lz or 5<=ly or 5<=lx or visbfs[lz][ly][lx]!=0 or B[lz][ly][lx]!=1:
                    continue
                visbfs[lz][ly][lx]=visbfs[z][y][x]+1
                dq.append([lz,ly,lx])



    
import sys
from collections import deque
input=sys.stdin.readline
board=[[list(map(int, input().strip().split())) for i in range(5)] for j in range(5)]
dx=[0,0,0,1,0,-1]
dy=[0,0,-1,0,1,0]
dz=[-1,1,0,0,0,0]
li=[0,0,0,0,0]
johap=[0,0,0,0,0]
vis=[False]*5
dq=deque([])
answer=[]
rotationboard=[[rotation(board[j], k) for k in range(4)] for j in range(5)] #j는 5*5 0~4번까지 맵, k는 j번째의 k회 회전 모양
# print(*rotationboard[0][0], sep='\n\n')
mixture(0)
if len(answer)==0:
    print(-1)
else:
    print(min(answer))