import sys
from collections import deque
input=sys.stdin.readline
N, M, K=list(map(int, input().strip().split()))
board=[list(map(int, input().strip().split())) for _ in range(N)] #고정값
trees=deque([list(map(int, input().strip().split())) for _ in range(M)])
food=[[5 for i in range(N)] for j in range(N)]
garden=[[[] for i in range(N)] for j in range(N)]
dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]
while trees:
    tmp=trees.popleft()
    garden[tmp[0]-1][tmp[1]-1].append(tmp[2])
# print(*garden, sep='\n')

for season in range(K):
    #봄
    for i in range(N):
        for j in range(N):
            if garden[i][j]==[]:
                continue
            garden[i][j].sort()
            for le in range(len(garden[i][j])):
                if garden[i][j][le]<=food[i][j]:
                    food[i][j]-=garden[i][j][le]
                    garden[i][j][le]+=1
                else:
                    for _ in range(len(garden[i][j])-le):
                        food[i][j]+=garden[i][j].pop()//2 #여름
                    break
    # print(*garden, sep='\n')
    # print(*food, sep='\n')      봄여름 잘 지나갔나 확인
    #가을
    for i in range(N):
        for j in range(N):
            food[i][j]+=board[i][j] #겨울
            if garden[i][j]==[]:
                continue
            for le in range(len(garden[i][j])):
                if garden[i][j][le]%5==0:
                    for z in range(8):
                        y=i+dy[z]
                        x=j+dx[z]
                        if y<0 or x<0 or N<=y or N<=x:
                            continue
                        garden[y][x].append(1)
            
    #겨울
    # for i in range(N):
    #     for j in range(N):
            
    # print(*food, sep='\n')

#확인
cnt=0
for i in range(N):
    for j in range(N):
        if len(garden[i][j])!=0:
            cnt+=len(garden[i][j])
print(cnt)