def bod(y, x, N):
    if N==1:
        li[board[y][x]]+=1
        return

    half=N//3
    for i in range(y,y+N):
        for j in range(x,x+N):
            if board[y][x]!=board[i][j]:
                bod(y, x, half)
                bod(y, x+half, half)
                bod(y, x+half*2, half)
                bod(y+half, x, half)
                bod(y+half, x+half, half)
                bod(y+half, x+half*2, half)
                bod(y+half*2, x, half)
                bod(y+half*2, x+half, half)
                bod(y+half*2, x+half*2, half)
                return
    li[board[y][x]]+=1
    return
    
import sys
input= sys.stdin.readline
N=int(input().strip())
board=[list(map(int,input().strip().split())) for _ in range(N)]
li=[0]*3
bod(0,0,N)
print(li[-1])
print(li[0])
print(li[1])