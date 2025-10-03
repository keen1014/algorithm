def ch_base(num, k, st):
        mok, nam=divmod(num,k)
        st=str(nam)+st
        if mok>0:
            return ch_base(mok, k, st)
        return st
    
    
def is_prime(li):
    cnt=0
    for i in li:
        if i==2:
            cnt+=1
        elif 2<i:
            for j in range(2,int(i**(1/2))+1):
                if i%j==0:
                    break
            else:
                cnt+=1
    return cnt
    
def solution(n, k):
    result=list(map(int,' '.join(ch_base(n,k, '').split('0')).split()))
    return is_prime(result)