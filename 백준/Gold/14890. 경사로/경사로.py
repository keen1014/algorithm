def serch(list):
    global ans
    cnt=1
    answer=deque([])
    for i in range(N-1):
        if list[i]==list[i+1]:
            cnt+=1
        else:
            answer.append([list[i],cnt])
            cnt=1
    else:
        answer.append([list[-1],cnt])
    # print(answer)
    while answer:
        tmp=answer.popleft()
        if answer:
            if abs(answer[0][0]-tmp[0])==1:
                if answer[0][0]<tmp[0]:
                    if L<=answer[0][1]:
                        answer[0][1]-=L
                    else:
                        break
                elif tmp[0]<answer[0][0]:
                    if L<=tmp[1]:
                        continue
                        
                    else:
                        break
            else:
                break
        else:
            continue
    else:
        ans+=1
import sys
from collections import deque
input=sys.stdin.readline
N, L=map(int, input().strip().split())
board=[list(map(int, input().strip().split())) for i in range(N)]
# print(*board, sep='\n', end='\n\n')
li=[0]*N
ans=0
for i in range(N):
    for j in range(N):
        li[j]=board[j][i]
    serch(li)
    serch(board[i])
print(ans)