import sys
input=sys.stdin.readline
n=int(input().strip())
dp=[[0 for _ in range(n)] for i in range(n)]
dp[0][0]=int(input().strip())
for i in range(1,n):
    li=list(map(int,input().strip().split()))+[0]
    dp[i][0]=dp[i-1][0]+li[0]
    for j in range(1,len(li)-1):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+li[j]

print(max(dp[n-1]))