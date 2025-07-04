def ziper(N, y, x):
    if N==1:
        stack.append(board[y][x])
        return
    for i in range(N):
        for j in range(N):
            if board[y][x]!=board[y+i][x+j]:
                stack.append('(')
                ziper(N//2, y, x)
                ziper(N//2, y, x+N//2)
                ziper(N//2, y+N//2, x)
                ziper(N//2, y+N//2, x+N//2)
                stack.append(')')
                return
    stack.append(board[y][x])
    return


    
import sys
input=sys.stdin.readline
N=int(input().strip())
board=[list(map(int, input().strip())) for i in range(N)]
stack=[]
ziper(N, 0, 0)
print(*stack, sep='')