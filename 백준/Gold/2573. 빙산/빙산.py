import sys
from collections import deque
input=sys.stdin.readline
N, M= map(int, input().strip().split())
ice=[list(map(int, input().strip().split()))for i in range(N)]
vis=[[False]*M for j in range(N)]
ice_loc=set()
new_ice_loc=[]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
dq=deque([])
year=0

for i in range(N):
    for j in range(M):
        if ice[i][j]!=0:
            ice_loc.add((i,j))
while ice_loc:
    e=ice_loc.pop()
    dq.append(e)
    ice_loc.add(e)
    vis[e[0]][e[1]]=True
    imsi=set()
    imsi.add(e)
    while dq:
        tmp=dq.popleft()
        for k in range(4):
            x=dx[k]+tmp[1]
            y=dy[k]+tmp[0]
            if x<0 or y<0 or x>=M or y>=N or ice[y][x]==0 or vis[y][x]==True:
                continue
            else:
                vis[y][x]=True
                dq.append([y,x])
                imsi.add((y,x))

    # 2조각으로 나뉘면 끝
    if ice_loc!=imsi:
        print(year)
        break
    
    year+=1
    
    
    # 빙산의 녹는 정도 확인 후 업데이트
    while ice_loc:
        tmp=ice_loc.pop()
        sea=0
        for k in range(4):
            x=dx[k]+tmp[1]
            y=dy[k]+tmp[0]
            if x<0 or y<0 or x>=M or y>=N or ice[y][x]!=0:
                continue
            elif ice[y][x]==0:
                sea+=1
        if ice[tmp[0]][tmp[1]]-sea>0:
            new_ice_loc.append([tmp[0], tmp[1], ice[tmp[0]][tmp[1]]-sea])
            vis[tmp[0]][tmp[1]]=False
        else:
            new_ice_loc.append([tmp[0], tmp[1], 0])
            vis[tmp[0]][tmp[1]]=False
    # ice_loc 채우기 
    while new_ice_loc:
        tmp=new_ice_loc.pop()
        ice[tmp[0]][tmp[1]]=tmp[2]
        if tmp[2]!=0:
            ice_loc.add((tmp[0], tmp[1]))
else:
    print(0)