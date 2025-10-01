from collections import deque
def solution(str1, str2):
    tmp1=deque([])
    tmp2=deque([])
    li1=[]
    li2=[]
    h1={}
    h2={}
    for i in range(len(str1)):
        if 'A'<=str1[i]<='Z' or 'a'<=str1[i]<='z':
            if 'a'<=str1[i]<='z':
                if len(tmp1)<2:
                    tmp1.append(str1[i].upper())
                else:
                    tmp1.append(str1[i].upper())
                    tmp1.popleft()
            else:
                if len(tmp1)<2:
                    tmp1.append(str1[i])
                else:
                    tmp1.append(str1[i])
                    tmp1.popleft()
            if len(tmp1)==2:
                t=tuple(tmp1.copy())
                li1.append(t)
        else:
            tmp1=deque([])
    for i in range(len(str2)):
        if 'A'<=str2[i]<='Z' or 'a'<=str2[i]<='z':
            if 'a'<=str2[i]<='z':
                if len(tmp2)<2:
                    tmp2.append(str2[i].upper())
                else:
                    tmp2.append(str2[i].upper())
                    tmp2.popleft()
            else:
                if len(tmp2)<2:
                    tmp2.append(str2[i])
                else:
                    tmp2.append(str2[i])
                    tmp2.popleft()
            if len(tmp2)==2:
                t=tuple(tmp2.copy())
                li2.append(t)
        else:
            tmp2=deque([])
    if li1==[] and li2==[]:
        return 65536;
    for i in set(li1):
        h1[i]=0
    for i in set(li2):
        h2[i]=0
    for i in li1:
        h1[i]+=1
    for i in li2:
        h2[i]+=1
    k=0
    h=0
    sub=0
    njip=list(set(li1)&set(li2))
    for ky in njip:
        k+=min(h1[ky], h2[ky])
        h+=max(h1[ky], h2[ky])
        sub+=(h1[ky]+h2[ky])
    h=sum(h1.values())+sum(h2.values())+h-sub
    return int((k/h)*65536)