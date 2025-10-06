def solution(stones, k):
    answer=0
    def is_zero(n):
        nonlocal k
        cnt=0
        for i in range(len(stones)):
            if stones[i]<n:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                return False
        else:
            return True
    S=0
    E=200_000_000
    now=100_000_000
    while S<=E:
        now=(E+S)//2 
        if True==is_zero(now):
            S=now+1
            answer = now
        else:
            E=now-1
    
    return answer