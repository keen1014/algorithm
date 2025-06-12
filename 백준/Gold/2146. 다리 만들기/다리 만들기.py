import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
board=[list(map(int, input().strip().split())) for i in range(N)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
outline=set()
ground_cnt=1
sea_cnt=0
m=[]
vis_ground=[([0]*N)for i in range(N)]
ground_dq=deque([])
sea_dq=deque([])
for i in range(N):
    for j in range(N):
        if board[i][j]==1 and vis_ground[i][j]==0:
            ground_dq.append([i, j])
            vis_ground[i][j]=1
            ground_cnt+=1
            while ground_dq:
                tmp=ground_dq.pop()
                for k in range(4):
                    x=tmp[1]+dx[k]
                    y=tmp[0]+dy[k]
                    if x<0 or y<0 or x>=N or y>=N or (board[y][x]==1 and vis_ground[y][x]!=0):
                        continue
                    elif board[y][x]==0:
                        outline.add((tmp[0], tmp[1], ground_cnt))
                    else:
                        ground_dq.append([y, x])
                        vis_ground[y][x]=vis_ground[tmp[0]][tmp[1]]+1

vis_sea=[([0]*N)for i in range(N)]
outline=deque(outline)
while outline:
    tmp=outline.popleft()
    for k in range(4):
        x=tmp[1]+dx[k]
        y=tmp[0]+dy[k]
        if x<0 or y<0 or x>=N or y>=N or board[y][x]==1 or vis_sea[y][x]!=0 and board[y][x]==tmp[2]:
            continue
        elif vis_sea[y][x]!=0 and board[y][x]!=tmp[2]:
            m.append(vis_sea[tmp[0]][tmp[1]]+vis_sea[y][x])
            break
        else:
            vis_sea[y][x]=vis_sea[tmp[0]][tmp[1]]+1
            board[y][x]=tmp[2]
            outline.append([y,x,tmp[2]])
print(min(m))