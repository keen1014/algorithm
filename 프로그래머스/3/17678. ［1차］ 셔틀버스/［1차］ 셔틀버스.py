from collections import deque
def solution(n, t, m, timetable):
    answer=''
    li=deque([])
    busli=[]
    maxtime=24*60
    mornningbus=9*60
    for i in timetable:
        hh,mm=list(map(int,i.split(':')))
        li.append(hh*60+mm)
    li=sorted(li)
    li=deque(li)
    for j in range(n):
        busli.append(mornningbus+j*t)
    tmp=0
    for bus in range(len(busli)):
        tmpli=[]
        while li and li[0]<=busli[bus]:
            tmpli.append(li.popleft())
            if len(tmpli)==m:
                break
        if bus==len(busli)-1:
            if len(tmpli)<m:
                H, M=divmod(busli[bus],60)
                answer=str(H).zfill(2)+':'+str(M).zfill(2)
            else:
                H, M=divmod(tmpli[-1]-1,60)
                answer=str(H).zfill(2)+':'+str(M).zfill(2)
    return answer