cnt=0
def bubun(N, M):
    global cnt
    if N==n:
        if M==s:
            cnt+=1
        return
    bubun(N+1, M)
    bubun(N+1, M+numlist[N])
    return
    
import sys
input=sys.stdin.readline
n, s= map(int, input().strip().split())
numlist=list(map(int,input().strip().split()))
vis=[False]*n
bubun(0, 0)
if s==0:
    print(cnt-1)
else:
    print(cnt)