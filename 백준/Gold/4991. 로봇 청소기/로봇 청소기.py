def BFS(dist1, dist2):
    dq=deque([dist1])
    bd=[[-1 for _ in range(C)] for _ in range(R)]
    bd[dist1[0]][dist1[1]]=0
    while dq:
        tmp=dq.popleft()
        for i in range(4):
            y=tmp[0]+dy[i]
            x=tmp[1]+dx[i]
            if y<0 or x<0 or R<=y or C<=x or board[y][x]=='x' or bd[y][x]!=-1:
                continue
            bd[y][x]=bd[tmp[0]][tmp[1]]+1
            dq.append([y,x])
        if bd[dist2[0]][dist2[1]]!=-1:
            return bd[dist2[0]][dist2[1]]
    return -1
import sys
from collections import deque
input=sys.stdin.readline
dx=[0,1,0,-1]
dy=[-1,0,1,0]
while True:
    C,R=list(map(int, input().strip().split()))
    if R==0 and C==0:
        break
    board=[list(input().strip()) for _ in range(R)]
    # print(*board, sep='\n',end='\n\n')
    dust=deque([])
    stx=0
    sty=0
    answer=[]
    for i in range(R):
        for j in range(C):
            if board[i][j]=='o':
                stx=j
                sty=i
            elif board[i][j]=='*':
                dust.append([i,j])
    dust.appendleft([sty,stx])
    dists=[[-1 for j in range(len(dust))] for i in range(len(dust))]
    bitmask=[[float('inf') for j in range(len(dust))] for i in range(2**len(dust))]
    #BFS는 두 좌표를 받아서 거리계산 후 리턴 불가능일 경우 -1
    boo=False
    for i in range(len(dust)):
        for j in range(len(dust)):
            tmp=BFS(dust[i], dust[j])
            if tmp==-1:
                print(-1)
                boo=True
                break
            dists[i][j]=tmp
            dists[j][i]=tmp
            
            
        if boo==True:
            break
    if boo:
        continue
    
    bitmask[2**0][0]=0
    
    for i in range(2**len(dust)):
        for j in range(len(dust)):
            if bitmask[i][j]==float('inf'):
                continue


            for k in range(len(dust)):
                if not (i & (1<<k)==1<<k):
                    newsh=i+(1<<k)
                    newlen=bitmask[i][j]+dists[k][j]
                    bitmask[newsh][k]=min(bitmask[newsh][k],newlen)

    print(min(bitmask[2**len(dust)-1]))