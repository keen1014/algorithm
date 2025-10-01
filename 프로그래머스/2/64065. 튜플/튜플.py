def solution(s):
    answer = []
    tmp=[]
    s=s.replace('{', '')
    s=s.replace(',', ' ')
    s=s.split('}')
    li=[]
    ans=[]
    for i in range(len(s)):
        s[i]=s[i].split(' ')
        for j in s[i]:
            if j =='':
                continue
            tmp.append(int(j))
        if tmp!=[]:
            answer.append(tmp)
        tmp=[]
    answer.sort(key= lambda answer: len(answer))
    for j in answer:
        for k in j:
            if k not in ans:
                ans.append(k)
    return ans