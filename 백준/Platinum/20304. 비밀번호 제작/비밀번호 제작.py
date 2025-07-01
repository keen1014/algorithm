import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
M=int(input().strip())
p=list(map(int, input().strip().split()))
dq=deque([])
le=len(bin(N)[2:])
cnt=0
vis=[0 for i in range(N+1)]
for i in range(M):
    dq.append(p[i])
    vis[p[i]]=1
while True:
    if dq:
        for _ in range(len(dq)):
            tmp=dq.popleft()
            imsi=1
            for j in range(le):
                if imsi^tmp<0 or N<imsi^tmp or vis[imsi^tmp]!=0:
                    imsi=imsi << 1
                    continue
                dq.append(imsi^tmp)
                vis[imsi^tmp]=1
                imsi=imsi << 1
    else:
        print(cnt-1)
        break
    cnt+=1