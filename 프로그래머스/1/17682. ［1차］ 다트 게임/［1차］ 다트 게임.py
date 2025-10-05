from collections import deque
def solution(dartResult):
    num=[]
    sang=[]
    option=[]
    n=0
    tmp=dartResult.split('S')
    tmp=' '.join(tmp)
    tmp=tmp.split('D')
    tmp=' '.join(tmp)
    tmp=tmp.split('T')
    tmp=' '.join(tmp)
    tmp=tmp.split('*')
    tmp=' '.join(tmp)
    tmp=tmp.split('#')
    tmp=' '.join(tmp)
    tmp=list(map(int, tmp.split()))
    num=tmp
    tmp2=dartResult.split(f'{num[0]}')
    tmp2=' '.join(tmp2)
    tmp2=tmp2.split(f'{num[1]}')
    tmp2=' '.join(tmp2)
    tmp2=tmp2.split(f'{num[2]}')
    tmp2=' '.join(tmp2)
    tmp2=tmp2.split()
    print(num)
    print(tmp2)
    for i in range(len(num)):
        tmp2[i]=deque(tmp2[i])
        while tmp2[i]:
            scr=tmp2[i].popleft()
            if scr=='S':
                num[i]=num[i]**1
            elif scr=='D':
                num[i]=num[i]**2
            elif scr=='T':
                num[i]=num[i]**3
            elif scr == '*':
                if i==0:
                    num[i]=num[i]*2
                else:
                    num[i]=num[i]*2
                    num[i-1]=num[i-1]*2
            elif scr == '#':
                num[i]=num[i]*-1
    answer = sum(num)
    return answer