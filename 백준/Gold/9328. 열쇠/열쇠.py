import sys
from collections import deque
input=sys.stdin.readline
case=int(input().strip())
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
for _ in range(case):
    dq=deque([])
    alpha=[deque([]) for i in range(26)]
    h, w=map(int, input().strip().split())
    board=[list(input().strip()) for i in range(h)]
    vis=[[0 for i in range(w)] for j in range(h)]
    key=list(input().strip())
    havekeynum=[0 for i in range(26)]

    cnt=0
    for i in range(h):
        for j in range(w):
            if 'A'<=board[i][j]<'a':
                alpha[ord(board[i][j])-65].append([i,j])
            if i==0 or i==h-1:
                if 'a'<=board[i][j]<='z':
                    havekeynum[ord(board[i][j])-65-32]+=1
                if board[i][j]!='*':
                    dq.append([i,j])
            elif j==0 or j==w-1:
                if 'a'<=board[i][j]<='z':
                    havekeynum[ord(board[i][j])-65-32]+=1
                if board[i][j]!='*':
                    dq.append([i,j])

    for k in key:
        if k=='0':
            break
        havekeynum[ord(k)-32-65]+=1
        
    for z in range(len(dq)):
        tmp=dq.popleft()
        if board[tmp[0]][tmp[1]]=='.' or (board[tmp[0]][tmp[1]]!='.' and 65<=ord(board[tmp[0]][tmp[1]])<97 and 0<havekeynum[ord(board[tmp[0]][tmp[1]])-65]) or 'z' >= board[tmp[0]][tmp[1]] >= 'a' or board[tmp[0]][tmp[1]]=='$':
            dq.append(tmp)
            vis[tmp[0]][tmp[1]]=1
            if board[tmp[0]][tmp[1]]=='$':
                cnt+=1

    if dq:
        while dq:
            tmp=dq.popleft()
            for i in range(4):
                x=dx[i]+tmp[1]
                y=dy[i]+tmp[0]
                if 0>x or 0>y or x>=w or y>=h or board[y][x]=='*' or vis[y][x]==1:
                    continue
                elif 'A'<=board[y][x]<'a':
                    if 0<havekeynum[ord(board[y][x])-65]:
                        dq.append([y,x])
                        vis[y][x]=1
                elif board[y][x]=='$':
                    dq.append([y,x])
                    vis[y][x]=1
                    cnt+=1
                elif board[y][x]=='.':
                    dq.append([y,x])
                    vis[y][x]=1
                elif 'a'<=board[y][x]<='z':
                    dq.append([y,x])
                    vis[y][x]=1
                    while alpha[ord(board[y][x])-65-32]:
                        imsi=alpha[ord(board[y][x])-65-32].pop()
                        board[imsi[0]][imsi[1]]='.'
                        if imsi[0]==0 or imsi[0]==h-1 or imsi[1]==0 or imsi[1]==w-1:#새로운 문이 열림:
                                dq.append(imsi)
                                vis[imsi[0]][imsi[1]]=1
                        for j in range(4):
                            ix=dx[j]+imsi[1]
                            iy=dy[j]+imsi[0]
                            if 0>ix or 0>iy or ix>=w or iy>=h or board[iy][ix]=='*':
                                continue
                            elif vis[iy][ix]==1:
                                dq.append(imsi)
                                vis[imsi[0]][imsi[1]]=1
        print(cnt)
    else:
        print(0)