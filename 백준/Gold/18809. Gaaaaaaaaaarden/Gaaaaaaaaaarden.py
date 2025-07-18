max=0
max_seedGR=0
def seeds(n, start):
    global max
    if n==G+R:
        tmp=seedGR(0, 0)
        if max<tmp:
            max=tmp
        return
    for i in range(start, len(dq)):
        if not vis[i]:
            vis[i]=True
            li[n]=dq[i]+[0]
            seeds(n+1, i+1)
            vis[i]=False

def seedGR(n, start):
    global max_seedGR
    if n==G:
        for z in range(G+R):
            if vis_li[z]==False:
                li[z]=['R']+li[z]
        tmp=BFS(li)
        if max_seedGR<tmp:
            max_seedGR=tmp
        for z in range(G+R):
            if vis_li[z]==False:
                li[z]=li[z][1:]
    for i in range(start, G+R):
        if not vis_li[i]:
            vis_li[i]=True
            li[i]=['G']+li[i]
            seedGR(n+1, i+1)
            vis_li[i]=False
            li[i]=li[i][1:]
    return max_seedGR
            
def BFS(list):
    cnt=0
    s=deque(list)
    visited=[[[0, 0]for _ in range(M)] for _ in range(N)]
    for p in range(len(s)):
        zc, zy, zx, znum=s[p]
        visited[zy][zx]=[zc, znum]
    while s:
        for z in range(len(s)):
            c, y, x, num=s.popleft()
            if visited[y][x][0]!='flower':
                for i in range(4):
                    ny=y+dy[i]
                    nx=x+dx[i]
                    if nx<0 or ny<0 or M<=nx or N<=ny or board[ny][nx]==0:
                        continue
                    if visited[ny][nx]==[0,0]:
                        visited[ny][nx]=[c, num+1]
                        s.append([c, ny, nx, num+1])
                    elif visited[ny][nx][1]==num+1 and visited[ny][nx][0]!=c and (visited[ny][nx][0]=='G' or visited[ny][nx][0]=='R'):
                        cnt+=1
                        visited[ny][nx]=['flower', cnt]
    return cnt

import sys
from collections import deque
dq=deque([])
ground=deque([])
input=sys.stdin.readline
N, M, G, R=map(int,input().strip().split())
board=[list(map(int, input().strip().split())) for i in range(N)]
# 0: 호수, 1: 뿌릴 수 없는 땅, 2: 가능

li=['']*(G+R)
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            dq.append([i,j])
        if board[i][j]==1:
            ground.append([i,j])
vis=[False]*(len(dq))
vis_li=[False]*(G+R)
seeds(0, 0)
print(max)
# 중복조합을 허용한 백트래킹을 돌려서 토양을 가져옴
# R, G가 만약 3, 2 라면 R, R, R, G, G 순서로 고정을 하고 백트래킹
# BFS를 돌리면서 확인