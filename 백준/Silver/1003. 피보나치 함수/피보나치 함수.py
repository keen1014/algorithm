import sys
input=sys.stdin.readline
T=int(input().strip())
dp=[[0,0] for _ in range(41)]
dp[0]=[1, 0]
dp[1]=[0, 1]
for j in range(2,40+1):
    dp[j]=[dp[j-1][0]+dp[j-2][0],dp[j-1][1]+dp[j-2][1]]
for i in range(T):
    print(*dp[int(input().strip())])