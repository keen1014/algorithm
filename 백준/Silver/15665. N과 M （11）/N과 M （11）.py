def nm(N):
    if N==m:
        print(*li)
        return
    remember_num=0
    for i in range(n):
        if not vis[i] and remember_num!=stack[i]:
            li[N]=stack[i]
            remember_num=stack[i]
            nm(N+1)
import sys
input=sys.stdin.readline
n, m=map(int, input().strip().split())
stack=sorted(list(map(int, input().strip().split())))
vis=[False]*n
li=[0]*m
nm(0)