import sys
from collections import deque
input=sys.stdin.readline
N, K=map(int, input().strip().split())
dq=deque([N])
vis=[[-1 for i in range(500001)] for j in range(2)]
vis[0][N]=0 #0 짝, 1홀
dx=[-1, 1]
move=0
cnt=0
answer=[]
if N==K:
    print(0)
    exit()
while True:
    move=move+cnt+1
    target=K+move
    cnt+=1
    hj=cnt%2
    if target>=500001:
        print(-1)
        exit()
    if dq:
        for _ in range(len(dq)):
            tmp=dq.popleft()
            for i in range(2):
                x=dx[i]+tmp
                if 0>x or x>500000 or vis[hj][x]!=-1:
                    continue
                vis[hj][x]=cnt
                dq.append(x)
                
            x=tmp*2
            if 0>x or x>500000 or vis[hj][x]!=-1:
                continue
            vis[hj][x]=cnt
            dq.append(x)        
        if vis[hj][target]!=-1:
            print(cnt)
            exit()
    else:
        print(-1)
        exit()