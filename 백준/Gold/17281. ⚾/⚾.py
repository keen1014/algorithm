def playininning():
    now=0
    ans=0
    for z in range(N):
        ru1=ru2=ru3=out=0
        while out!=3:
            tmp=li[now]
            ins=inning[z][tmp]
            
            if ins==0:
                out+=1
            elif ins== 1:
                ans+=ru3
                ru1, ru2, ru3= 1, ru1, ru2
                
            elif ins== 2:
                ans+=(ru3+ru2)
                ru1, ru2, ru3= 0, 1, ru1
            elif ins== 3:
                ans+=(ru3+ru2+ru1)
                ru1, ru2, ru3= 0, 0, 1
            elif ins== 4:
                ans+=(ru3+ru2+ru1+1)
                ru1, ru2, ru3= 0, 0, 0
            now+=1
            if 9<=now:
                now=0

        answer.add(ans)
        
def backtracking(n):
    if n == 9:
        # print(li)
        playininning()
        return
    for i in range(9):
        if i==0 or vis[i]==True:
            continue
        vis[i]=True
        if 3==n:
            li[n+1]=i
            backtracking(n+2)
        else:
            li[n]=i
            backtracking(n+1)
        vis[i]=False
        
import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
li=[0]*9
vis=[False]*9
answer=set()
inning=[list(map(int, input().strip().split())) for i in range(N)]
# print(*inning, sep='\n')
backtracking(0)
print(max(answer))