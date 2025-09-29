from collections import deque
def solution(record):
    dq=deque(record)
    user={}
    answer = []
    for i in range(len(dq)):
        tmp=dq.popleft()
        tmp=tmp.split()
        if tmp[0]=='Enter' or tmp[0]=='Change':
            user[tmp[1]]=tmp[2]
        dq.append([tmp[0],tmp[1]])
    while dq:
        tmp=dq.popleft()
        if tmp[0]=='Enter':
            answer.append(f"{user[tmp[1]]}님이 들어왔습니다.")
        elif tmp[0]=='Leave':
            answer.append(f"{user[tmp[1]]}님이 나갔습니다.")
    return answer