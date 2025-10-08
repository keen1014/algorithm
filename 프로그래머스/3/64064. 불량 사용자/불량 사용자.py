import itertools
def solution(user_id, banned_id):
    li=[]
    for i in banned_id:
        tmp=[]
        for j in range(len(user_id)):
            if len(user_id[j])==len(i):
                for k in range(len(i)):
                    if i[k]=='*':
                        continue
                    elif i[k]!=user_id[j][k]:
                        break
                else:
                    tmp.append(user_id[j])
        li.append(tmp)
    allcombi=list(itertools.product(*li))
    # print(allcombi)
    unique=[combo for combo in allcombi if len(set(combo)) == len(combo)]
    setli=[]
    for uni in unique:
        tmp=sorted(uni)
        if tmp not in setli:
            setli.append(tmp)
    answer = len(setli)
    return answer