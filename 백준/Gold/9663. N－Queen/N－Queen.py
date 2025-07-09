cnt=0
def queen(N):
    global cnt
    if N==n:
        cnt+=1
        return
    for i in range(n):
        if not vis[i] and not ldru[N+i] and not lurd[i-N+n-1]:
            vis[i]=True
            board[N][i]=1
            ldru[N+i]=True
            lurd[i-N+n-1]=True
            queen(N+1)
            ldru[N+i]=False
            lurd[i-N+n-1]=False
            board[N][i]=0
            vis[i]=False


            
import sys
input=sys.stdin.readline
n= int(input().strip())
board=[[0]*n for i in range(n)]
vis=[False]*n
ldru=[False]*(n*2)
lurd=[False]*(n*2)
queen(0)
print(cnt)