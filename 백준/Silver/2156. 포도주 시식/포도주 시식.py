import sys
input=sys.stdin.readline
N=int(input().strip())
dp=[[0,0] for i in range(N)]
ans=0
for i in range(N):
    n=int(input().strip())
    if i-2<0:
        dp[i][0]=n
        if ans<dp[i][0]:
            ans=dp[i][0]
    else:
        if dp[i-2][1]+n<dp[i-2][0]+n:
            dp[i][0]=dp[i-2][0]+n
        else:
            dp[i][0]=dp[i-2][1]+n
        if dp[i][0]<dp[i-3][1]+n:
            dp[i][0]=dp[i-3][1]+n
        if ans<dp[i][0]:
            ans=dp[i][0]
    if 0<i:
        dp[i][1]=dp[i-1][0]+n
    if ans<dp[i][1]:
            ans=dp[i][1]
print(ans)