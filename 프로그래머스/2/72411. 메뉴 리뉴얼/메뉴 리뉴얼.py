import itertools
def solution(orders, course):
    answer = []
    for i in course:
        dic ={}
        for j in orders:
            j=sorted(j)
            li=list(itertools.combinations(j,i))
            for k in li:
                k=''.join(k)
                if k in dic.keys():
                    dic[k]+=1
                else:
                    dic[k]=1
        if dic:
            m=max(dic.values())
            for z, v in dic.items():
                if 2<=v and v == m:
                    answer.append(z)
        answer=sorted(answer)
    return answer