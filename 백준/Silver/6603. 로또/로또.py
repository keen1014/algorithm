def gambling(N):
    if N==6:
        print(*li)
        return
    for i in range(k):
        if not vis[i]:
            if N==0 or N!=0 and li[N-1]<dq[i]:
                vis[i]=True
                li[N]=dq[i]
                gambling(N+1)
                vis[i]=False


        
import sys
from collections import deque
input=sys.stdin.readline
li=[0]*6
while True:
    dq=deque(list(map(int, input().strip().split())))
    if dq[0]==0:
        break
    k=dq.popleft()
    vis=[False]*k
    gambling(0)
    print()