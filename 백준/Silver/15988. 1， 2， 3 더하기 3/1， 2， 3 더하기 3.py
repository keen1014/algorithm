import sys
input=sys.stdin.readline
dp=[0]*1000001
dp[0]=1
dp[1]=2
dp[2]=4
T=int(input().strip())
for i in range(3,1000001):
    dp[i]=(dp[i-3]+dp[i-2]+dp[i-1])%1000000009
# n=int(input().strip())
for i in range(T):
    n=int(input().strip())
    print(dp[n-1])