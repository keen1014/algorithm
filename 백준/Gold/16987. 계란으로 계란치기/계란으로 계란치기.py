cnt=0
max=0
def breakegg(n):
    global cnt, max
    if n==N:
        if max<cnt:
            max=cnt
        return
    if not br[n]:
        for i in range(N):
            if n==i or br[i]==True:
                continue
            tmp1=egg[n][0]
            br3=br[n]
            tmp2=egg[i][0]
            br4=br[i]
            tmpcnt=cnt
            if egg[n][0]-egg[i][1]<=0:
                br[n]=True
                cnt+=1
            if egg[i][0]-egg[n][1]<=0:
                br[i]=True
                cnt+=1
            egg[n][0]=egg[n][0]-egg[i][1]
            egg[i][0]=egg[i][0]-egg[n][1]
            
            breakegg(n+1)
            egg[n][0]=tmp1
            egg[i][0]=tmp2
            br[n]=br3
            br[i]=br4
            cnt=tmpcnt
        else:
            if max<cnt:
                max=cnt
    elif br[n]:
        breakegg(n+1)
import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
egg={}
br=[False]*N
for i in range(N):
    egg[i]=list(map(int,input().strip().split()))
breakegg(0)
print(max)