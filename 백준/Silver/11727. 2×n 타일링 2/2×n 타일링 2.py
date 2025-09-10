import sys
input=sys.stdin.readline
n=int(input().strip())
dp=[0 for i in range(1001)]
dp[1]=1
if 1<n:
    dp[2]=3
for j in range(3,n+1):
    dp[j]=(dp[j-1]+2*dp[j-2])%10007
print(dp[n])