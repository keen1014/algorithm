import sys
input=sys.stdin.readline
T=int(input().strip())
dp=[0]*101
dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2
dp[6]=3
for j in range(7,101):
        dp[j]=dp[j-5]+dp[j-1]
for i in range(T):
    n=int(input().strip())
    print(dp[n])
    