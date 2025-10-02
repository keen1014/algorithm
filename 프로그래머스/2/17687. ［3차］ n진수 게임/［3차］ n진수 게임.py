def solution(n, t, m, p):
    def to_base(n, base):
        digits = '0123456789ABCDEF'
        if n == 0:
            return '0'
        result = ''
        while n != 0:
            n, r = divmod(n, base)
            result = digits[r] + result
        return result

    result = ''  # 전체 나열된 숫자들
    num = 0
    while len(result) < t * m:
        result += to_base(num, n)
        num += 1

    answer = ''
    for i in range(t):
        answer += result[(p - 1) + i * m]

    print(answer)
    return answer
'''
def solution(n, t, m, p):
    number=0
    mok=0
    cnt=1
    answer = []
    while len(answer)<t:
        if mok==0 and p==1:
            answer.append(0)
            number+=1
        while mok!=0:
            mok,nam=divmod(mok,n)
            if cnt==p:
                if 10<=nam:
                        answer.append(hex(nam)[2].upper())
                else:
                    answer.append(nam)
            if cnt==m:
                cnt=1
            else:
                cnt+=1
            
        number+=1
        mok=number
    print(answer)
    return answer
'''
'''
def solution(n, t, m, p):
    number=0
    cnt=1
    mo=0
    answer = []
    if p==1: # 0부터 시작하는 애들이 0 출력하는것 그럼 다른애들은 1부터 시작해야함
        answer.append(0)
        cnt+=1
    else:
        cnt+=1
        mo=1
        number+=1
    while len(answer)!=t:
        while mo!=0:
            mo,re=(divmod(mo,n))
            if cnt==p:
                if 10<=re:
                    answer.append(hex(re)[2].upper())
                else:
                    answer.append(re)
            
            if cnt==m:
                cnt=1
            else:
                cnt+=1
        
        number+=1
        mo=number
        
    print(*answer, sep='')
    return answer
'''