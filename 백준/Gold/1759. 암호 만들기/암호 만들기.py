def password(N,j,m):
    if N==L and 2<=j and 1<=m:
        print(*li, sep='')
        return
    elif N==L:
        return
    for i in range(C):
        if (N==0 and not vis[i]) or (not vis[i] and N!=0 and ord(li[N-1])<ord(s[i])):
            vis[i]=True
            li[N]=s[i]
            if s[i] in moum:
                password(N+1,j,m+1)
            else:
                password(N+1,j+1,m)
            vis[i]=False
import sys
input=sys.stdin.readline
L, C=map(int, input().strip().split())
s=sorted(list(input().strip().split()))
vis=[False]*C
li=[0]*L
moum=['a', 'e', 'i', 'o', 'u']
password(0,0,0)