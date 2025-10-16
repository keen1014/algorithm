import sys
input=sys.stdin.readline
cnt=1
while True:
    board=[]
    t=int(input().strip())
    dp=[[0 for k in range(3)]for i in range(t+1)]
    if t==0:
        break
    for j in range(t):
        board.append(list(map(int, input().strip().split())))
    dp[0][0]=float('inf')
    dp[0][1]=board[0][1]
    dp[0][2]=board[0][1]+board[0][2]
    for z in range(1, t):
        dp[z][0]=board[z][0]+min(dp[z-1][0],dp[z-1][1])
        dp[z][1]=board[z][1]+min(dp[z][0], dp[z-1][0],dp[z-1][1],dp[z-1][2])
        dp[z][2]=board[z][2]+min(dp[z][1], dp[z-1][2],dp[z-1][1])
    print(f'{cnt}. {dp[t-1][1]}')
    cnt+=1