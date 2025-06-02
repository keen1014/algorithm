import sys
from collections import deque
input=sys.stdin.readline
F, S, G, U, D= list(map(int, input().strip().split()))
stack=[0 for i in range(F)]
dq=deque([])
dq.append(S)
stack[S-1]=1
while dq:
    tmp=dq.popleft()
    u=tmp+U
    d=tmp-D
    if u>0 and u<=F and stack[u-1] ==0:
        dq.append(u)
        stack[u-1]=stack[tmp-1]+1
    if d>0 and stack[d-1] == 0:
        dq.append(d)
        stack[d-1]=stack[tmp-1]+1
if S==G:
    print(0)
elif stack[G-1]==0:
    print('use the stairs')
else:
    print(stack[G-1]-1)