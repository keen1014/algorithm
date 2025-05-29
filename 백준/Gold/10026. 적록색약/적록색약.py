import sys
from collections import deque
input=sys.stdin.readline
dq=deque([])
n=int(input().strip())
m=[list(input().strip()) for _ in range(n)]
vis=[[0 for i in range(n)]for _ in range(n)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
cnt=0
for i in range(n):
    for j in range(n):
        if m[i][j]=='R' and vis[i][j]==0:
            dq.append(['R', i, j])
            vis[i][j]=1
            cnt+=1
        elif m[i][j]=='G' and vis[i][j]==0:
            dq.append(['G', i, j])
            vis[i][j]=1
            cnt+=1
        elif m[i][j]=='B' and vis[i][j]==0:
            dq.append(['B', i, j])
            vis[i][j]=1
            cnt+=1
        while dq:
            tmp=dq.popleft()
            if tmp[0]=='R':
                for z in range(4):
                    x=dx[z]+tmp[2]
                    y=dy[z]+tmp[1]
                    if x<0 or y<0 or x>=n or y>=n or m[y][x]!='R' or (m[y][x]=='R' and vis[y][x]==1):
                        continue
                    else:
                        dq.append(['R', y, x])
                        vis[y][x]=1
            elif tmp[0]=='G':
                for z in range(4):
                    x=dx[z]+tmp[2]
                    y=dy[z]+tmp[1]
                    if x<0 or y<0 or x>=n or y>=n or m[y][x]!='G'or (m[y][x]=='G' and vis[y][x]==1):
                        continue
                    else:
                        dq.append(['G', y, x])
                        vis[y][x]=1
            elif tmp[0]=='B':
                for z in range(4):
                    x=dx[z]+tmp[2]
                    y=dy[z]+tmp[1]
                    if x<0 or y<0 or x>=n or y>=n or m[y][x]!='B' or (m[y][x]=='B' and vis[y][x]==1):
                        continue
                    else:
                        dq.append(['B', y, x])
                        vis[y][x]=1
print(cnt)
cnt =0
for i in range(n):
    for j in range(n):
        if m[i][j]=='R':
            dq.append(['R', i, j])
            m[i][j]='r'
            cnt+=1
        elif m[i][j]=='G':
            dq.append(['R', i, j])
            m[i][j]='r'
            cnt+=1
        elif m[i][j]=='B':
            dq.append(['B', i, j])
            m[i][j]='b'
            cnt+=1
        while dq:
            tmp=dq.popleft()
            if tmp[0]=='R':
                for z in range(4):
                    x=dx[z]+tmp[2]
                    y=dy[z]+tmp[1]
                    if x<0 or y<0 or x>=n or y>=n or (m[y][x]!='R' and m[y][x]!='G'):
                        continue
                    else:
                        dq.append(['R', y, x])
                        m[y][x]='r'
            elif tmp[0]=='B':
                for z in range(4):
                    x=dx[z]+tmp[2]
                    y=dy[z]+tmp[1]
                    if x<0 or y<0 or x>=n or y>=n or m[y][x]!='B':
                        continue
                    else:
                        dq.append(['B', y, x])
                        m[y][x]='b'
print(cnt)