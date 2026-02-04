import sys
input=sys.stdin.readline
N=int(input())
dp=[0]*300001
dp[1]=1
for i in range(2, 300001):
    dp[i]=dp[i-1]+i
dp2=[0]*300001
dp2[1]=1
li=[0, 1]
for i in range(2, 300001):
    if 300000<dp[i]+dp2[i-1]:
        break
    dp2[i]=dp[i]+dp2[i-1]
    li.append(dp[i]+dp2[i-1])


dp3=[float('inf')]*300001
dp3[0]=0
for t in li:
    for j in range(t, N+1):
        if dp3[j-t]+1 < dp3[j]:
            dp3[j]= dp3[j-t]+1
print(dp3[j])
