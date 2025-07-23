def comparison(i, j):
    for k in range(i,R+i):
        for z in range(j, C+j):
            if sticker[k-i][z-j]==1 and board[k][z]==0 or sticker[k-i][z-j]== 0:
                continue
            else:
                return False
    else:
        return True
        
def attach(i, j):
    for k in range(i,R+i):
        for z in range(j, C+j):
            if sticker[k-i][z-j]==1:
                board[k][z]=1
                
def rotation(r, c, list):
    rtboard=[[0 for i in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            rtboard[j][r-1-i]=list[i][j]
    return c, r, rtboard
import sys
input=sys.stdin.readline
cnt=0
N, M, K= map(int, input().strip().split())
board =[[0 for i in range(M)] for j in range(N)]
for _ in range(K):
    R, C= map(int, input().strip().split())
    flag=False
    sticker= [list(map(int, input().strip().split())) for i in range(R)]
    for _ in range(4):
        for i in range(N-R+1):
            if flag:
                break
            for j in range(M-C+1):
                flag=comparison(i, j)
                if flag:
                    attach(i, j)
                    break
        if not flag:
            R, C, sticker=rotation(R, C, sticker)

            

for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            cnt+=1
        
print(cnt)