import sys
from collections import deque
input= sys.stdin.readline
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
repeat= int(input().strip())
for _ in range(repeat):
    fdq=deque([])
    pdq=deque([])
    m=[]
    f=[]
    p=[]
    w, h=map(int, input().strip().split())
    for i in range(h):
        m.append(list(input().strip()))
        f.append([0 for j in range(w)])
        p.append([0 for j in range(w)])
    for i in range(h):
        for j in range(w):
            if m[i][j]=='*':
                fdq.append([i, j])
                f[i][j]=1
            elif m[i][j] == '@':
                pdq.append([i, j])
                p[i][j]=1
    while fdq:
        tmp=fdq.popleft()
        for k in range(4):
            x=dx[k]+tmp[1]
            y=dy[k]+tmp[0]
            if x<0 or y<0 or x>=w or y>=h or f[y][x]!=0 or m[y][x]=='#':
                continue
            else:
                f[y][x]=f[tmp[0]][tmp[1]]+1
                fdq.append([y, x])
    while pdq:
        tmp=pdq.popleft()
        if tmp[1]==0 or tmp[0]==0 or tmp[1]==w-1 or tmp[0]==h-1:
            print(p[tmp[0]][tmp[1]])
            break
        for k in range(4):
            x=dx[k]+tmp[1]
            y=dy[k]+tmp[0]
            if x<0 or y<0 or x>=w or y>=h or p[y][x]!=0 or m[y][x]=='#' or (f[y][x] !=0 and f[y][x]<=p[tmp[0]][tmp[1]]+1):
                continue
            else:
                p[y][x]=p[tmp[0]][tmp[1]]+1
                pdq.append([y, x])
    else:
        print('IMPOSSIBLE')