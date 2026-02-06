import sys
from collections import deque
input=sys.stdin.readline
N, K =map(int, input().split())
li=list(map(int, input().split()))
a_li=sorted(li)
dq=deque([(li,0)])
vis=set()
vis.add("".join(map(str, li)))
while dq:
    templi, v=dq.popleft()
    if templi==a_li:
        print(v)
        break
    for i in range(N-K+1):
        temp=templi[:i]+templi[i:i+K][::-1]+templi[i+K:]
        if "".join(map(str, temp)) in vis:
            continue
        vis.add("".join(map(str, temp)))
        dq.append((temp, v+1))
else:
    print(-1)