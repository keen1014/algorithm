def nm(N):
    if N==m:
        print(*li)
        return
    for i in range(n):
        if not vis[i]:
            li[N]=i+1
            nm(N+1)
import sys
input=sys.stdin.readline
n, m=map(int, input().strip().split())
vis=[False]*n
li=[0]*m
nm(0)