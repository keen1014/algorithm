import collections
def solution(p):
    def rightstr(s):
        dq=collections.deque([])
        for i in range(len(s)):
            if s[i]=='(':
                dq.append(s[i])
            elif dq and dq[-1]=='(' and s[i]==')':
                dq.pop()
            else:
                return False
        return True
    
    def re(s):
        dic=collections.defaultdict(int)
        u=''
        v=''
        if s=='':
            return ''
        for i, val in enumerate(s):
            dic[val]+=1
            if dic['(']!=0 and dic['(']==dic[')']:
                u=s[:i+1]
                v=s[i+1:]
                if rightstr(u)==True:
                    return u+re(v)
                else:
                    tmp='('
                    tmp=tmp+re(v)+')'
                    u=u[1:-1]
                    utmp=''
                    for j in u:
                        if j=='(':
                            utmp+=')'
                        else:
                            utmp+='('
                    return tmp+utmp
    answer = re(p)
    return answer