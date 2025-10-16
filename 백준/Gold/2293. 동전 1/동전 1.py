import sys
input=sys.stdin.readline
n, k=list(map(int, input().strip().split()))
li=[]
dp=[0 for j in range(100001)]
for i in range(n):
    li.append(int(input().strip()))
dp[0]=1
li=sorted(li)
for z in range(n):
    for x in range(li[z],k+1):
        dp[x]+=dp[x - li[z]]
print(dp[k])