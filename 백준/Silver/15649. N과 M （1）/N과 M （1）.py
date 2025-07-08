def nm(N):
    if N==m:
        print(*stack)
        return
    for i in range(0,n):
        if not vis[i]:
            vis[i]=True
            stack[N]=i+1
            nm(N+1)
            vis[i]=False


import sys
input=sys.stdin.readline

n, m= map(int, input().strip().split())
stack=[0]*m
vis=[False]*n
nm(0)