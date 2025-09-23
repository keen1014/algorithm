import sys
input=sys.stdin.readline
T, W = list(map(int, input().strip().split()))
dp=[[[0,0]for j in range(W+1)]for i in range(T)]
n=int(input().strip())
if n==1:
    dp[0][0][0]=1
else:
    dp[0][1][1]=1

for i in range(1,T):
    n=int(input().strip())
    for j in range(W+1):
        if j==0:
            dp[i][0][0]=dp[i-1][0][0]
            if n == 1:
                dp[i][0][0]+=1
            continue
        if n==1:
            dp[i][j][0]=max(dp[i-1][j][0], dp[i-1][j-1][1])+1
            dp[i][j][1]=max(dp[i-1][j][1], dp[i-1][j-1][0])
        else:
            dp[i][j][0]=max(dp[i-1][j][0], dp[i-1][j-1][1])
            dp[i][j][1]=max(dp[i-1][j][1], dp[i-1][j-1][0])+1
# print(*dp, sep='\n')
print(max(max(dp[T-1])))