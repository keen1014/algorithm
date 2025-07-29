def turn(tnum, d):
    if tnum<0 or 4<=tnum:
        return
    if tnum<3 and t[tnum][2]!=t[tnum+1][6]:
        turn(tnum+1, -d)
    if d==1:
        li.append([tnum, d])
    elif d==-1:
        li.append([tnum, d])
def turnl(tnum, d):
    if tnum<0 or 4<=tnum:
        return
    if 0<tnum and t[tnum][6]!=t[tnum-1][2]:
        turnl(tnum-1, -d)
    if d==1:
        li.append([tnum, d])
    elif d==-1:
        li.append([tnum, d])
import sys
from collections import deque
t=[deque(list(map(int, input().strip()))) for i in range(4)]
K=int(input().strip())
answer=0
for i in range(K):
    li=[]
    setli=[]
    tn, dir=list(map(int, input().strip().split()))
    turn(tn-1, dir)
    turnl(tn-1, dir)
    for i in range(len(li)):
        if li[i] not in setli:
            setli.append(li[i])
    while setli:
        tnum, tdir=setli.pop()
        if tdir==1:
            t[tnum].appendleft(t[tnum].pop())
        elif tdir==-1:
            t[tnum].append(t[tnum].popleft())

if t[0][0]==1:
    answer+=1
if t[1][0]==1:
    answer+=2
if t[2][0]==1:
    answer+=4
if t[3][0]==1:
    answer+=8
print(answer)