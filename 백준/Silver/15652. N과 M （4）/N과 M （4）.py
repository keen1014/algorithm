def nm(N, x):
    if N==m:
        print(*li)
        return
    for i in range(x, n):
        if not vis[i]:
            li[N]=i+1
            nm(N+1, i)
import sys
input=sys.stdin.readline
n, m=map(int, input().strip().split())
vis=[False]*n
li=[0]*m
nm(0, 0)