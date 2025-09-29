import sys
input=sys.stdin.readline
N=int(input().strip())
M=int(input().strip())
dp=[0]*(N+1)
dp[0]=1
dp[1]=1
for i in range(2, N+1):
    dp[i]=dp[i-1]+dp[i-2]
last_seat=0
result=1
for j in range(M):
    n=int(input().strip())
    result*=dp[n-last_seat-1]
    last_seat=n
result*=dp[N-last_seat]
print(result)