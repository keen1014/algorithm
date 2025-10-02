from collections import deque
def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        cnt=0
        miss=0
        for j in stages:
            if i<=j:
                if i==j:
                    miss+=1
                cnt+=1
        if miss==0 or cnt==0:
            answer.append([i,0])
        else:
            answer.append([i,miss/cnt])
        answer.sort(key=lambda x: x[1], reverse=True)
    ans=[]
    for tmp in answer:
        ans.append(tmp[0])
    return ans