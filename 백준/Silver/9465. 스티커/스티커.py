import sys
input=sys.stdin.readline
N=int(input().strip())
for i in range(N):
    m=int(input().strip())
    dp=[[0]*(m+2) for re in range(2)]
    l1=list(map(int, input().strip().split()))
    l2=list(map(int, input().strip().split()))
    for j in range(2, m+2):
        dp[0][j]=l1[j-2]+max(dp[1][j-1], dp[1][j-2])
        dp[1][j]=l2[j-2]+max(dp[0][j-1], dp[0][j-2])
    print(max(dp[0][m+1], dp[1][m+1]))