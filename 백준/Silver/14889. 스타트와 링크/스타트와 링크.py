def backtracking(n, ne):
    global ans, answer, halfN, liF
    if n==halfN:
        # print(li)
        for j in li:
            liF.remove(j)
        ST=0
        LT=0
        for k in li:
            for z in li:
                if z==k:
                    continue
                ST+=board[k][z]
        
        for k in liF:
            for z in liF:
                if z==k:
                    continue
                LT+=board[k][z]
        liF.update(li)
        a=abs(ST-LT)
        if a<answer:
            answer=a
        return
    for i in range(ne, N):
        if vis[i]==False:
            vis[i]=True
            li[n]=i
            backtracking(n+1, i+1)
            vis[i]=False

import sys
input= sys.stdin.readline
N=int(input().strip())
board=[list(map(int, input().strip().split()))for _ in range(N)]
halfN=N//2
ans=0
answer=100
liF=set(i for i in range(N))
vis=[False]*N
li=[-1]*halfN
backtracking(0, 0)
print(answer)