import sys
from collections import deque
N, M=map(int, input().split())
answer=M
group=[]
for i in range(N+1):
    group.append(i)
li=list(map(int, input().split()))
for z in li[1:]:
    group[z]=-1

dic={}
for z in range(1,N+1):
    dic[z]=set()
loop=[]

for _ in range(M):
    part=list(map(int, input().split()))
    loop.append(part[1:])
    for r in range(1, part[0]):
        for z in range(r+1, len(part)):
            dic[part[r]].add(part[z])
            dic[part[z]].add(part[r])
# print(dic)
# print(group)
for s in dic:
    if group[s]==-1:
        dq=deque([dic[s]])
        while dq:
            tmpli=[]
            tmp=dq.popleft()
            for l in tmp:
                if group[l]==-1:
                    continue
                group[l]=-1
                for c in dic[l]:
                    tmpli.append(c)
            if tmpli!=[]:
                dq.append(tmpli)
        # print(dic[s])
# print(dic)
# print(group)
for lo in loop:
    for x in lo:
        if group[x]==-1:
            answer-=1
            break
print(answer)