def solution(msg):
    dic={}
    answer = []
    for i in range(65, 91):
        dic[chr(i)]=i-64
    z=0
    while z!=len(msg)+1:
        for j in range(z+1, len(msg)+1):
            if msg[z:j] not in dic.keys():
                dic[msg[z:j]]=len(dic)+1
                answer.append(dic[msg[z:j-1]])
                z=j-1
                break
            elif msg[z:j] in dic.keys() and j==len(msg):
                answer.append(dic[msg[z:j]])
                return answer
        else:
            z+=1
    return answer