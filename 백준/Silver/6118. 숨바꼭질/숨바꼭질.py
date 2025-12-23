import sys
from collections import defaultdict
from collections import deque
input=sys.stdin.readline
N, M= map(int, input().strip().split())
dic=defaultdict(list)
li=[0]*(N)
ansli=[]
for i in range(M):
    Ai, Bi = map(int, input().strip().split())
    dic[Ai].append(Bi)
    dic[Bi].append(Ai)
dq=deque([[1]])
vis=[False]*(N+1)
cnt=0
max_cnt=0
while dq:
    tmp=dq.popleft()
    imsi=[]
    for room in tmp:
        if not vis[room]:
            vis[room]=True
            li[room-1]=cnt
            if max_cnt<cnt:
                max_cnt=cnt
                ansli=[room]
            elif max_cnt==cnt:
                ansli.append(room)
            for z in dic[room]:
                imsi.append(z)
    if imsi:
        dq.append(imsi)
    cnt+=1
ansli.sort()
print(ansli[0], li[ansli[0]-1], len(ansli))