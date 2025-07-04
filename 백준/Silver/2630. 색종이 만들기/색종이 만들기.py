def paper(N, y, x):
    if N==1:
        li[board[y][x]]+=1
        return
    for i in range(N):
        for j in range(N):
            if board[y][x]!=board[i+y][j+x]:
                paper(N//2,y,x)
                paper(N//2,y,x+N//2)
                paper(N//2,y+N//2,x)
                paper(N//2,y+N//2,x+N//2)
                return
    li[board[y][x]]+=1
    return
    

    
import sys
input=sys.stdin.readline
N=int(input().strip())
board=[list(map(int, input().split())) for i in range(N)]
li=[0]*2
paper(N, 0, 0)
print(*li,sep='\n')