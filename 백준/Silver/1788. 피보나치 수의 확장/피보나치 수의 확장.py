import sys
input=sys.stdin.readline
n=int(input().strip())
dp=[0 for i in range(1_000_001)]
dp[0]=0
dp[1]=1
dp[2]=1
dp[3]=2
for i in range(4, 1_000_001):
    dp[i]=(dp[i-1]+dp[i-2])%1_000_000_000
if n==0:
    print(0)
    print(0)
elif n<0 and n%2==0:
    print(-1)
    print(dp[abs(n)])
else:
    print(1)
    print(dp[abs(n)])