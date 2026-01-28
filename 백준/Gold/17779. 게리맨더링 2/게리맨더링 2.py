import sys
input=sys.stdin.readline
N=int(input().strip())
board=[]
answer=float('inf')
total=0
for _ in range(N):
    board.append(list(map(int, input().split())))

total=sum(map(sum, board))
# x는 1부터 x+d1+d2<=N이 되는걸 다 찾아야하고
# y는 1=<y-d1<y<y+d2<=N 이 성립되는 것을 찾아야한다.
# d1은 0 가능
# d2는 1부터 가능
# 결국 경계선은 5번 구역임
def move(x, y, d1, d2):
    newboard=[[0]*N for _ in range(N)]
    for z in range(d1+1):
        newboard[x+z][y-z]=5 #1
        newboard[x+d2+z][y+d2-z]=5 #4
    for z in range(d2+1):
        newboard[x+z][y+z]=5 #2
        newboard[x+d1+z][y-d1+z]=5 #3


            
    group=[0]*5
    for i in range(x+d1):
        for j in range(y+1):
            if newboard[i][j]==5:
                break
            group[0]+=board[i][j]
            
    for i in range(x+d2+1):
        for j in range(N-1, y, -1):
            if newboard[i][j]==5:
                break
            group[1]+=board[i][j]
            
    for i in range(x+d1,N):
        for j in range(y-d1+d2):
            if newboard[i][j]==5:
                break
            group[2]+=board[i][j]
            
    for i in range(x+d2+1, N):
        for j in range(N-1, y-d1+d2-1, -1):
            if newboard[i][j]==5:
                break
            group[3]+=board[i][j]
            
    group[4]=total-sum(group)
    return max(group)-min(group)

for d1 in range(1, N):
    for d2 in range(1, N):
        for ix in range(N-2):
                for iy in range(1, N-1):
                    if ix+d1+d2 < N and 0 <= iy-d1 and iy+d2<N:
                        # print("d1:",d1, " d2:",d2, " x:",ix, " y:",iy)
                        temp=move(ix, iy, d1, d2)
                        if answer>temp:
                            answer=temp
print(answer)