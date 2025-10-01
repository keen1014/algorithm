from collections import deque
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        li=deque([])
        for j in range(n):
            tmp1=divmod(arr1[i],2)
            arr1[i]=tmp1[0]
            tmp2=divmod(arr2[i],2)
            arr2[i]=tmp2[0]
            if tmp1[1]==1 or tmp2[1]==1:
                li.appendleft('#')
            else:
                li.appendleft(' ')
        li=''.join(li)
        answer.append(li)
    return answer