def solution(numbers, hand):
    answer = ''
    L=[3,0]
    R=[3,2]
    for i in numbers:
        if i==1:
            answer+='L'
            L=[0,0]
        elif i==4:
            answer+='L'
            L=[1,0]
        elif i==7:
            answer+='L'
            L=[2,0]
        elif i==3:
            answer+='R'
            R=[0,2]
        elif i==6:
            answer+='R'
            R=[1,2]
        elif i==9:
            answer+='R'
            R=[2,2]
        elif i==2 or i==5 or i==8 or i==0:
            if i==2:
                n2=[0,1]
                if (abs(n2[0]-L[0])+abs(n2[1]-L[1]))==(abs(n2[0]-R[0])+abs(n2[1]-R[1])):
                    if hand=='left':
                        answer+='L'
                        L=n2
                    elif hand=='right':
                        answer+='R'
                        R=n2
                elif (abs(n2[0]-L[0])+abs(n2[1]-L[1]))<(abs(n2[0]-R[0])+abs(n2[1]-R[1])):
                    answer+='L'
                    L=n2
                elif (abs(n2[0]-R[0])+abs(n2[1]-R[1]))<(abs(n2[0]-L[0])+abs(n2[1]-L[1])):
                    answer+='R'
                    R=n2
            elif i==5:
                n5=[1,1]
                if (abs(n5[0]-L[0])+abs(n5[1]-L[1]))==(abs(n5[0]-R[0])+abs(n5[1]-R[1])):
                    if hand=='left':
                        answer+='L'
                        L=n5
                    elif hand=='right':
                        answer+='R'
                        R=n5
                elif (abs(n5[0]-L[0])+abs(n5[1]-L[1]))<(abs(n5[0]-R[0])+abs(n5[1]-R[1])):
                    answer+='L'
                    L=n5
                elif (abs(n5[0]-R[0])+abs(n5[1]-R[1]))<(abs(n5[0]-L[0])+abs(n5[1]-L[1])):
                    answer+='R'
                    R=n5
            elif i==8:
                n8=[2,1]
                if (abs(n8[0]-L[0])+abs(n8[1]-L[1]))==(abs(n8[0]-R[0])+abs(n8[1]-R[1])):
                    if hand=='left':
                        answer+='L'
                        L=n8
                    elif hand=='right':
                        answer+='R'
                        R=n8
                elif (abs(n8[0]-L[0])+abs(n8[1]-L[1]))<(abs(n8[0]-R[0])+abs(n8[1]-R[1])):
                    answer+='L'
                    L=n8
                elif (abs(n8[0]-R[0])+abs(n8[1]-R[1]))<(abs(n8[0]-L[0])+abs(n8[1]-L[1])):
                    answer+='R'
                    R=n8
            elif i==0:
                n0=[3,1]
                if (abs(n0[0]-L[0])+abs(n0[1]-L[1]))==(abs(n0[0]-R[0])+abs(n0[1]-R[1])):
                    if hand=='left':
                        answer+='L'
                        L=n0
                    elif hand=='right':
                        answer+='R'
                        R=n0
                elif (abs(n0[0]-L[0])+abs(n0[1]-L[1]))<(abs(n0[0]-R[0])+abs(n0[1]-R[1])):
                    answer+='L'
                    L=n0
                elif (abs(n0[0]-R[0])+abs(n0[1]-R[1]))<(abs(n0[0]-L[0])+abs(n0[1]-L[1])):
                    answer+='R'
                    R=n0
            
        
    
    return answer