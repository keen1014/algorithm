import sys
from collections import deque
input=sys.stdin.readline
N, M=map(int, input().split())
ball={}
ball2={}
answer1=[0]*(N+1)
answer2=[0]*(N+1)
answer=0
for i in range(1,N+1):
    ball[i]=[] #가벼운거
    ball2[i]=[]#무거운거
for i in range(M):
    b1, b2=map(int, input().split())
    ball[b1].append(b2)
    ball2[b2].append(b1)


for i in range(1,N+1):
    vis=[False]*(N+1)
    vis[i]=True
    dq=deque([i])
    while dq:
        tmp=dq.popleft()
        for z in ball[tmp]:
            if vis[z]:
                continue
            dq.append(z)
            answer1[i]+=1
            vis[z]=True



for i in range(1,N+1):
    vis=[False]*(N+1)
    vis[i]=True
    dq=deque([i])
    while dq:
        tmp=dq.popleft()
        for z in ball2[tmp]:
            if vis[z]:
                continue
            dq.append(z)
            answer2[i]+=1
            vis[z]=True
# print(answer1)
# print(answer2)
for x in range(1,N+1):
    if (N+1)//2<=answer1[x] or (N+1)//2<=answer2[x]:
        answer+=1
print(answer)