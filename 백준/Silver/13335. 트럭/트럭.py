import sys
from collections import deque
input=sys.stdin.readline
nw=deque([])
answer=0
bridgew=0
n, w, L = map(int, input().strip().split())
a=deque(list(map(int,input().strip().split())))
while a:
    de=False
    if nw:
        for i in range(len(nw)):
            nw[i][1]-=1
            if nw[i][1]==0:
                bridgew-=nw[i][0]
                de=True
        if de:
            nw.popleft()
    if len(nw)<w and a[0]+bridgew<=L:
        tmp=a.popleft()
        bridgew+=tmp
        nw.append([tmp,w])
    answer+=1
print(answer+w)