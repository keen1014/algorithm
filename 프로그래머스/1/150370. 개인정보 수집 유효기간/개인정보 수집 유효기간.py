def solution(today, terms, privacies):
    answer = []
    dic={}
    tmp=today.split('.')
    today=int(tmp[0])*12*28+int(tmp[1])*28+int(tmp[2])
    for i in terms:
        k,v=i.split()
        dic[k]=int(v)*28

    for cnt, j in enumerate(privacies):
        pri, ke=j.split()
        pri=pri.split('.')
        dday=int(pri[0])*12*28+int(pri[1])*28+int(pri[2])
        if (dday+dic[ke])<=today:
            answer.append(cnt+1)
    return answer