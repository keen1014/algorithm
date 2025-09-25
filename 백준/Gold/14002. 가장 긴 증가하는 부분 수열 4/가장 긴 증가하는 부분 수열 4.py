import sys
import copy
input=sys.stdin.readline
N=int(input().strip())
A=list(map(int, input().strip().split()))
dp=[[] for i in range(N)]
# print(A)
ans=1
ansli=[A[0]]
dp[0].append(A[0])
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if dp[j][-1]<A[i] and len(dp[i])<=len(dp[j]):
            dp[i]=dp[j].copy()
            continue
    dp[i].append(A[i])
    if ans<len(dp[i]):
        ans=len(dp[i])
        ansli=dp[i]
# print(dp)
print(ans)
print(*ansli)