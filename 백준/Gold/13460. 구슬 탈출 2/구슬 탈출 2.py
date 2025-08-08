def move(y, x, dly, dlx, cnt):
    while True:
        if board[y+dly][x+dlx]=='#':
            break
        elif board[y][x]=='O':
            break
        y+=dly
        x+=dlx
        cnt+=1
    return y, x, cnt


    
import sys
from collections import deque
input= sys.stdin.readline
N,M=map(int, input().strip().split())
board=[list(input().strip())for i in range(N)]
dq=deque([])
answer=0
# print(*board, sep='\n')
vis=[]
R=[]
B=[]
O=[]
end=[False,False]
for i in range(N):
    for j in range(M):
        if board[i][j]=='R':
            R=[i, j]
        elif board[i][j]=='B':
            B=[i, j]
        elif board[i][j]=='O':
            O=[i, j]
# print(R, B, O)
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
dq.append(R)
dq.append(B)
vis.append((R[0],R[1],B[0],B[1]))
while dq:
    answer+=1
    if 10<answer:
        print(-1)
        exit()
    for k in range(len(dq)//2):
        tmp=dq.popleft()
        tmp2=dq.popleft()
        for i in range(4):
            rly,rlx, rcnt=move(tmp[0],tmp[1],dy[i],dx[i], answer)
            bly,blx, bcnt=move(tmp2[0],tmp2[1],dy[i],dx[i], answer)
            if [rly,rlx]==[bly,blx] and [rly,rlx]!=O:
                if rcnt<bcnt:
                    bly-=dy[i]
                    blx-=dx[i]
                elif bcnt<rcnt:
                    rly-=dy[i]
                    rlx-=dx[i]
            elif [bly,blx]==O:
                continue
            elif [rly,rlx]==O:
                print(answer)
                exit()
            if (rly,rlx,bly,blx) in vis:
                continue
            dq.append([rly,rlx])
            dq.append([bly,blx])
print(-1)