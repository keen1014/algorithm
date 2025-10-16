import sys
input=sys.stdin.readline
n=int(input().strip())
dp=[0 for i in range(1_000_001)]
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=3
for i in range(4, n+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746
print(dp[n])