import sys
from collections import deque
input = sys.stdin.readline
dq= deque([])
ls=[-1 for i in range(100001)]
N, K= map(int, input().strip().split())
ls[N] = 0
dq.append(N)
while dq:
    tmp=dq.popleft()
    if tmp==K:
        print(ls[tmp])
        break
    if tmp*2<=100000:
        if ls[tmp*2]==-1:
            ls[tmp*2] = ls[tmp]+1
            dq.append(tmp*2)
    if tmp+1<=100000:
        if  ls[tmp+1]==-1:
            ls[tmp+1] = ls[tmp]+1
            dq.append(tmp+1)
    if tmp-1>=0:
        if  ls[tmp-1]==-1:
            ls[tmp-1] = ls[tmp]+1
            dq.append(tmp-1)