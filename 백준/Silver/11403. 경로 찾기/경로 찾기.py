from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
board=[]
answer=[[0 for i in range(N)] for j in range(N)]
dic=defaultdict(list)
for i in range(N):
    board.append(list(map(int, input().split())))
    for idx, v in enumerate(board[-1]):
        if v:
            dic[i].append(idx)

dq=deque()
for re in range(N):
    dq.append(re)
    while dq:
        tmp=dq.popleft()
        for z in dic[tmp]:
            if answer[re][z]:
                continue
            answer[re][z]=1
            dq.append(z)
for z in answer:
    print(*z)