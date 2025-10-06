from collections import deque
def solution(fees, records):
    m=1439
    dic={}
    answer = []
    for i in range(len(records)):
        records[i]=records[i].split()
        tmp1,tmp2=list(map(int, records[i][0].split(':')))
        records[i][0]=tmp1*60+tmp2
        if records[i][1] in dic.keys():
            dic[records[i][1]].append([records[i][0],records[i][2]])
        else:
            dic[records[i][1]]=deque([[records[i][0],records[i][2]]])
    
    for j in sorted(dic.keys()):
        number_score=0
        while dic[j]:
            tmp=dic[j].popleft()
            if tmp[1]=='IN' and dic[j]:
                number_score+=dic[j].popleft()[0]-tmp[0]
            elif tmp[1]=='IN' and not dic[j]:
                number_score+=m-tmp[0]
        if number_score<=fees[0]:
            answer.append(fees[1])
        else:
            mok, nam=divmod((number_score-fees[0]),fees[2])
            if nam!=0:
                mok+=1
            answer.append(fees[1]+mok*fees[3])
    return answer