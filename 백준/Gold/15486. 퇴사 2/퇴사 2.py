import sys
input=sys.stdin.readline
n=int(input().strip())
li=[[0,0]]
dp=[0]*(n+2)
for i in range(n):
    li.append(list(map(int, input().strip().split())))
    #TODO: 현재보다 작은 수들 중 가장 큰 값을 가져옴
for i in range(n, -1, -1):
    t=li[i][0]
    p=li[i][1]
    if n+1<i+t:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], p+dp[i+t])
print(dp[0])