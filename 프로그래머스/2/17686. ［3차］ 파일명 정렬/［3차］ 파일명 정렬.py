def solution(files):
    answer = []
    for idx,i in enumerate(files):
        tmp=[]
        jj=0
        for j in range(len(i)):
            if i[j].isdigit() and not tmp:
                tmp.append(i[:j])
                jj=j
            elif jj!=0 and (jj+5==j or not i[j].isdigit()):
                tmp.append(i[jj:j])
                tmp.append(i[j:])
                break
        else:
            tmp.append(i[jj:])
        tmp.append(idx)
        answer.append(tmp)
#                 n=0
#                 sice=i[j:]
                
                
#                 for z in range(len(sice)):
#                     if not sice[z].isdigit():
#                         tmp.append(sice[0:z])
#                         tmp.append(sice[z:])
#                         break
#                     if n==5 and sice[z].isdigit():
#                         tmp.append(sice[0:5])
#                         tmp.append(sice[5:])
#                         break
#                     n+=1
#                 else:
#                     tmp.append(sice[0:])
#                 tmp.append(idx)
#                 answer.append(tmp)
#                 # print(answer)
#                 break
                
    answer.sort(key=lambda x: (''.join(x[0]).upper(), int(x[1])))
    
    for i in range(len(answer)):
        answer[i]=''.join(answer[i][:-1])
    return answer