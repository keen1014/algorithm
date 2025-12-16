from collections import defaultdict
from collections import deque
import sys
import heapq
input=sys.stdin.readline
N, M, V= map(int, input().split())
dic=defaultdict(list)
for i in range(M):
    u, v =map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)
dq=deque([V])
vis1=[False]*(N+1)
vis2=[False]*(N+1)
li1=[]
li2=[]
while dq:
    tmp=dq.popleft()
    dic[tmp].sort()
    if vis1[tmp]:
        continue
    vis1[tmp]=True
    li1.append(tmp)
    for z in dic[tmp]:
        if vis1[z]:
            continue
        dq.append(z)

dq=deque([V])
while dq:
    tmp=dq.popleft()
    dic[tmp].sort(reverse=True)
    if vis2[tmp]:
        continue
    li2.append(tmp)
    vis2[tmp]=True
    for z in dic[tmp]:
        if vis2[z]:
            continue
        dq.appendleft(z)
print(*li2)
print(*li1)