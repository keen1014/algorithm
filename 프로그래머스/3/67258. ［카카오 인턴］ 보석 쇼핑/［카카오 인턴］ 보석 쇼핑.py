def solution(gems):
    setgems=set(gems)
    S=E=0
    dic={}
    answer = [100001,0,0]
    while S!=len(gems):
        if E!=len(gems) and len(dic.keys())!=len(setgems):
            if gems[E] not in dic.keys():
                dic[gems[E]]=1
            else:
                dic[gems[E]]+=1
            E+=1
            
        else:
            dic[gems[S]]-=1
            if dic[gems[S]]==0:
                del dic[gems[S]]
            S+=1
        if len(dic.keys())==len(setgems) and E-S<answer[0]:
                answer=[E-S,S+1,E]
    return answer[1:]

