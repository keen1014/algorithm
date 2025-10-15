import sys
input=sys.stdin.readline
N=int(input().strip())
dp=[[0 for z in range(10)] for s in range(1001)]
dp[1][0]=1
dp[1][1]=1
dp[1][2]=1
dp[1][3]=1
dp[1][4]=1
dp[1][5]=1
dp[1][6]=1
dp[1][7]=1
dp[1][8]=1
dp[1][9]=1
for i in range(2,N+1):
    for j in range(10):
        su=0
        for k in range(j+1):
            su+=dp[i-1][k]
        dp[i][j]=su
# dp[2]=55
# dp[3]=220
print(sum(dp[N])%10007)
