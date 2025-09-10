import sys
input=sys.stdin.readline
n=int(input().strip())
dp=[0 for i in range(n)]
li=list(map(int, input().strip().split()))
dp[0]=li[0]
for i in range(1,len(li)):
    tmp=dp[i-1]+li[i]
    if li[i]<tmp:
        dp[i]=tmp
    else:
        dp[i]=li[i]
print(max(dp))