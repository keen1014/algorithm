def nm(N):
    if N==m:
        print(*li)
        return
    for i in range(n):
        if not vis[i]:
            if N==0 or N!=0 and li[N-1]<stack[i]:
                vis[i]=True
                li[N]=stack[i]
                nm(N+1)
                vis[i]=False
import sys
input=sys.stdin.readline
n, m=map(int, input().strip().split())
stack=sorted(list(map(int, input().strip().split())))
vis=[False]*n
li=[0]*m
nm(0)