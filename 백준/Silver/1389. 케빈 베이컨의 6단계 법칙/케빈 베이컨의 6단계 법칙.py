from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
N, M=map(int, input().split())
u1=u2=0
dic=defaultdict(list)
min_ans=float('inf')
min_idx=0
answer=[99]*N
ansli=[]
for i in range(M):
    u1, u2=map(int, input().split())
    dic[u1].append(u2)
    dic[u2].append(u1)
dq=deque()
for i in range(1, N+1):
    vis=[-1]*N
    cnt=0
    vis[i-1]=cnt
    dq.append([i])
    while dq:
        cnt+=1
        tmp=dq.popleft()
        tmpli=[]
        for z in tmp:
            for x in dic[z]:
                if vis[x-1]!=-1:
                    continue
                vis[x-1]=cnt
                tmpli.append(x)
        if tmpli!=[]:
            dq.append(tmpli)
    if -1 not in vis:
        answer[i-1]=max(vis)
    if sum(vis)<min_ans:
        min_ans=sum(vis)
        min_idx=i
print(min_idx)