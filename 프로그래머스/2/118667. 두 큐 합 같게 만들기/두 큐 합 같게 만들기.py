from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    T1=sum(queue1)
    T2=sum(queue2)
    avg=T1+T2
    print(T1,T2,avg)
    S=0
    E=len(queue1)-1
    num=0
    while T1!=avg//2:
        if T1<avg//2:
            answer+=1
            E+=1
            tmp=queue2.popleft()
            T1+=tmp
            T2-=tmp
            queue1.append(tmp)
            num+=1
        elif avg//2<T1:
            answer+=1
            S-=1
            tmp=queue1.popleft()
            T1-=tmp
            T2+=tmp
            queue2.append(tmp)
            num+=1
        if 300000<num:
            return -1
    return answer