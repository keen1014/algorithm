def closedd(n,s):
    if n==M:
        answer.append(hus(li))
        return
    for i in range(s,len(chicken)):
        if not vis[n]:
            vis[n]=True
            li[n]=i
            closedd(n+1, i+1)
            vis[n]=False
            
def hus(li):
    total=[0]*len(house)
    for i in li:
        for j in range(len(house)):
            cy, cx = chicken[i]
            hy, hx= house[j]
            if total[j]==0:
                total[j]=abs(cy-hy)+abs(cx-hx)
            if total[j]!=0 and abs(cy-hy)+abs(cx-hx)<total[j]:
                total[j]=abs(cy-hy)+abs(cx-hx)
    return sum(total)
import sys
input=sys.stdin.readline
N, M= map(int, input().strip().split())
board=[list(map(int, input().strip().split())) for _ in range(N)]
li=[-1]*M
answer=[]
house=[]
chicken=[]
vis=[False]*M
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            house.append([i,j])
        elif board[i][j]==2:
            chicken.append([i,j])
closedd(0,0)
print(min(answer))