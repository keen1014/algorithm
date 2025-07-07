def star(y, x, N):
    if N==1:
        li[y][x]='*'
        return
    re=N//3
    star(y, x, re)
    star(y, x+re, re)
    star(y, x+(re)*2, re)
    star(y+re, x, re)
    star(y+(re), x+(re)*2, re)
    star(y+(re)*2, x, re)
    star(y+(re)*2, x+re, re)
    star(y+(re)*2, x+(re)*2, re)
    





    
import sys
input=sys.stdin.readline
N=int(input().strip())
li=[[' ']*N for i in range(N)]
star(0,0,N)
for i in range(N):
    print(''.join(li[i]))