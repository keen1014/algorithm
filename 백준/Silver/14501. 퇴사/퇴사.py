import sys
input=sys.stdin.readline
n=int(input().strip())
li=[[0,0]]
dp=[0]*(n+2)
for i in range(1,n+1):
    li.append(list(map(int, input().strip().split())))
    #TODO: 현재보다 작은 수들 중 가장 큰 값을 가져옴
    if li[i][0]+i<=n+1:
        for j in range(i+1):
            dp[li[i][0]+i]=max(dp[li[i][0]+i], dp[j]+li[i][1])

print(max(dp))