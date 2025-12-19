from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
u1=u2=0
dic=defaultdict(list)
li=[0]*N
answer=[99]*N
ansli=[]
while u1!=-1 and u2!=-1:
    u1, u2=map(int, input().split())
    #BFS
    if u1==-1 and u2==-1:
        continue
    dic[u1].append(u2)
    dic[u2].append(u1)
dq=deque()
for i in range(1, N+1):
    vis=[-1]*N
    cnt=0
    vis[i-1]=cnt
    dq.append([i])
    while dq!=deque():
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
min_ans=min(answer)
for i, v in enumerate(answer):
    if min_ans==v:
        ansli.append(i+1)
print(min_ans, len(ansli))
print(*ansli)