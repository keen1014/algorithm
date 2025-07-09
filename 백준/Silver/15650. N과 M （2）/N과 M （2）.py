def nm(n, x):
    if n==M:
        print(*li)
        return
    for i in range(x, N):
        if not vis[i]:
            vis[i]=True
            li[n]=i+1
            nm(n+1, i+1)
            vis[i]=False
            
import sys
input=sys.stdin.readline
N,M=map(int, input().strip().split())
vis=[False]*N
li=[0]*M
nm(0, 0)