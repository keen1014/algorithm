def star(y, x, N):
    if N==3:
        li[y][x]='*'
        li[y+1][x-1]='*'
        li[y+1][x+1]='*'
        li[y+2][x-2]='*'
        li[y+2][x-1]='*'
        li[y+2][x]='*'
        li[y+2][x+1]='*'
        li[y+2][x+2]='*'
        return
    star(y, x, N//2)
    star(y+N//2, x-N//2, N//2)
    star(y+N//2, x+N//2, N//2)
    return
import sys
input=sys.stdin.readline
N=int(input().strip())
li=[[' ']*(N*2-1) for i in range(N)]
star(0, N-1, N)
for i in range(N):
    print(''.join(li[i]))