import sys
input=sys.stdin.readline
n=int(input().strip())
li=list(map(int, input().strip().split()))
dp=[[0,0] for i in range(n)]
dp[0]=[li[0], li[0]]
answer=li[0]
for i in range(1, n):
    dp[i]=[li[i], li[i]]
    tmp=[0]
    for j in range(i-1,-1,-1):
        if dp[j][0]<li[i]:
            tmp.append(dp[j][1])
    dp[i]=[li[i], li[i]+max(tmp)]
    if answer<li[i]+max(tmp):
        answer=li[i]+max(tmp)
print(answer)