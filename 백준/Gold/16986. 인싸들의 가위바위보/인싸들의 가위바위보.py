import sys
from itertools import permutations
from collections import deque
input=sys.stdin.readline
N, K= map(int, input().split())
board=[]

for _ in range(N):
    board.append(list(map(int, input().split())))
kyon=list(map(int, input().split()))
minho=list(map(int, input().split()))


for jw in permutations(range(1, N+1)):
    victory=[0,0,0]
    idx=[0,0,0]
    bb=[list(jw)]
    bb.append(kyon)
    bb.append(minho)
    dq=deque([(0, 1)])
    while dq:
        if idx[0]>=N:
            break
        tmp=dq.popleft()
        wait=3-sum(tmp)
        if board[bb[tmp[0]][idx[tmp[0]]]-1][bb[tmp[1]][idx[tmp[1]]]-1]==0:
            victory[tmp[1]]+=1
            if victory[tmp[1]]==K and tmp[1]==0:
                print(1)
                exit()
            elif victory[tmp[1]]==K:
                break
            dq.append((tmp[1], wait))
            
        elif  board[bb[tmp[0]][idx[tmp[0]]]-1][bb[tmp[1]][idx[tmp[1]]]-1]==1:
            if tmp[0]<tmp[1]: 
                victory[tmp[1]]+=1
                if victory[tmp[1]]==K and tmp[1]==0:
                    print(1)
                    exit()
                elif victory[tmp[1]]==K:
                    break
                dq.append((tmp[1], wait))
            else:
                victory[tmp[0]]+=1
                if victory[tmp[0]]==K and tmp[0]==0:
                    print(1)
                    exit()
                elif victory[tmp[0]]==K:
                    break
                dq.append((tmp[0], wait))
            
            
        elif  board[bb[tmp[0]][idx[tmp[0]]]-1][bb[tmp[1]][idx[tmp[1]]]-1]==2:
            victory[tmp[0]]+=1
            if victory[tmp[0]]==K and tmp[0]==0:
                print(1)
                exit()
            elif victory[tmp[0]]==K:
                break
            dq.append((tmp[0], wait))
        
        idx[tmp[0]]+=1
        idx[tmp[1]]+=1
print(0)