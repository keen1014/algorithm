cnt=0
def backtracking(n):
    global cnt
    if n==len(cctv):
        arr.append(cnt)
        return
    y, x=cctv[n]
    if board[y][x]== 1:
        for dir in range(4):
            ly=y+dy[dir]
            lx=x+dx[dir]
            if ly<0 or lx<0 or N<=ly or M<=lx or board[ly][lx]==6:
                continue
            while(1):
                if ly<0 or lx<0 or N<=ly or M<=lx or board[ly][lx]==6:
                    break
                if vis[ly][lx]==0 and [ly,lx] not in cctv:
                    cnt-=1
                    vis[ly][lx]=(y, x)
                ly+=dy[dir]
                lx+=dx[dir]
                
            backtracking(n+1)
            while(1):
                ly-=dy[dir]
                lx-=dx[dir]
                if lx==x and ly==y:
                    break
                if vis[ly][lx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ly][lx]=0
                
    elif board[y][x]== 2:
        for dir in range(2):
            ly=y+dy[dir]
            lx=x+dx[dir]
            ky=y+dy[(dir+2)%4]
            kx=x+dx[(dir+2)%4]
            while(1):
                if ly<0 or lx<0 or N<=ly or M<=lx or board[ly][lx]==6:
                    break
                if vis[ly][lx]==0 and [ly,lx] not in cctv:
                    cnt-=1
                    vis[ly][lx]=(y, x)
                ly+=dy[dir]
                lx+=dx[dir]
            while(1):
                if ky<0 or kx<0 or N<=ky or M<=kx or board[ky][kx]==6:
                    break
                if vis[ky][kx]==0 and [ky,kx] not in cctv:
                    cnt-=1
                    vis[ky][kx]=(y, x)
                ky+=dy[(dir+2)%4]
                kx+=dx[(dir+2)%4]
                
            backtracking(n+1)
            
            while(1):
                ly-=dy[dir]
                lx-=dx[dir]
                if lx==x and ly==y:
                    break
                if vis[ly][lx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ly][lx]=0
            while(1):
                ky-=dy[(dir+2)%4]
                kx-=dx[(dir+2)%4]
                if kx==x and ky==y:
                    break
                if vis[ky][kx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ky][kx]=0
    elif board[y][x]== 3:
        for dir in range(4):
            ly=y+dy[dir]
            lx=x+dx[dir]
            ky=y+dy[(dir+1)%4]
            kx=x+dx[(dir+1)%4]
            while(1):
                if ly<0 or lx<0 or N<=ly or M<=lx or board[ly][lx]==6:
                    break
                if vis[ly][lx]==0 and [ly,lx] not in cctv:
                    cnt-=1
                    vis[ly][lx]=(y, x)
                ly+=dy[dir]
                lx+=dx[dir]
            while(1):
                if ky<0 or kx<0 or N<=ky or M<=kx or board[ky][kx]==6:
                    break
                if vis[ky][kx]==0 and [ky,kx] not in cctv:
                    cnt-=1
                    vis[ky][kx]=(y, x)
                ky+=dy[(dir+1)%4]
                kx+=dx[(dir+1)%4]
                
            backtracking(n+1)
            
            while(1):
                ly-=dy[dir]
                lx-=dx[dir]
                if lx==x and ly==y:
                    break
                if vis[ly][lx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ly][lx]=0
            while(1):
                ky-=dy[(dir+1)%4]
                kx-=dx[(dir+1)%4]
                if kx==x and ky==y:
                    break
                if vis[ky][kx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ky][kx]=0
                    
    elif board[y][x]== 4:
        for dir in range(4):
            ly=y+dy[dir]
            lx=x+dx[dir]
            ky=y+dy[(dir+1)%4]
            kx=x+dx[(dir+1)%4]
            my=y+dy[(dir+3)%4]
            mx=x+dx[(dir+3)%4]
            while(1):
                if ly<0 or lx<0 or N<=ly or M<=lx or board[ly][lx]==6:
                    break
                if vis[ly][lx]==0 and [ly, lx] not in cctv:
                    cnt-=1
                    vis[ly][lx]=(y, x)
                ly+=dy[dir]
                lx+=dx[dir]
            while(1):
                if ky<0 or kx<0 or N<=ky or M<=kx or board[ky][kx]==6:
                    break
                if vis[ky][kx]==0 and [ky,kx] not in cctv:
                    cnt-=1
                    vis[ky][kx]=(y, x)
                ky+=dy[(dir+1)%4]
                kx+=dx[(dir+1)%4]
            while(1):
                if my<0 or mx<0 or N<=my or M<=mx or board[my][mx]==6:
                    break
                if vis[my][mx]==0 and [my,mx] not in cctv:
                    cnt-=1
                    vis[my][mx]=(y, x)
                my+=dy[(dir+3)%4]
                mx+=dx[(dir+3)%4]
                
            backtracking(n+1)
            
            while(1):
                ly-=dy[dir]
                lx-=dx[dir]
                if lx==x and ly==y:
                    break
                if vis[ly][lx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ly][lx]=0
            while(1):
                ky-=dy[(dir+1)%4]
                kx-=dx[(dir+1)%4]
                if kx==x and ky==y:
                    break
                if vis[ky][kx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[ky][kx]=0
            while(1):
                my-=dy[(dir+3)%4]
                mx-=dx[(dir+3)%4]
                if mx==x and my==y:
                    break
                if vis[my][mx]==(y, x): #시작위치가 내것이라면
                    cnt+=1
                    vis[my][mx]=0

    elif board[y][x]== 5:
        ly=y+dy[0]
        lx=x+dx[0]
        ky=y+dy[(0+2)%4]
        kx=x+dx[(0+2)%4]
        my=y+dy[(0+3)%4]
        mx=x+dx[(0+3)%4]
        zy=y+dy[(0+1)%4]
        zx=x+dx[(0+1)%4]
        while(1):
            if ly<0 or lx<0 or N<=ly or M<=lx or board[ly][lx]==6:
                break
            if vis[ly][lx]==0 and [ly,lx] not in cctv:
                cnt-=1
                vis[ly][lx]=(y, x)
            ly+=dy[0]
            lx+=dx[0]
        while(1):
            if ky<0 or kx<0 or N<=ky or M<=kx or board[ky][kx]==6:
                break
            if vis[ky][kx]==0 and [ky,kx] not in cctv:
                cnt-=1
                vis[ky][kx]=(y, x)
            ky+=dy[(0+2)%4]
            kx+=dx[(0+2)%4]
        while(1):
            if my<0 or mx<0 or N<=my or M<=mx or board[my][mx]==6:
                break
            if vis[my][mx]==0 and [my,mx] not in cctv:
                cnt-=1
                vis[my][mx]=(y, x)
            my+=dy[(0+3)%4]
            mx+=dx[(0+3)%4]
        while(1):
            if zy<0 or zx<0 or N<=zy or M<=zx or board[zy][zx]==6:
                break
            if vis[zy][zx]==0 and [zy,zx] not in cctv:
                cnt-=1
                vis[zy][zx]=(y, x)
            zy+=dy[(0+1)%4]
            zx+=dx[(0+1)%4]
        backtracking(n+1)
        
        while(1):
            ly-=dy[0]
            lx-=dx[0]
            if lx==x and ly==y:
                break
            if vis[ly][lx]==(y, x): #시작위치가 내것이라면
                cnt+=1
                vis[ly][lx]=0
        while(1):
            ky-=dy[2]
            kx-=dx[2]
            if kx==x and ky==y:
                break
            if vis[ky][kx]==(y, x): #시작위치가 내것이라면
                cnt+=1
                vis[ky][kx]=0
        while(1):
            my-=dy[3]
            mx-=dx[3]
            if mx==x and my==y:
                break
            if vis[my][mx]==(y, x): #시작위치가 내것이라면
                cnt+=1
                vis[my][mx]=0
        while(1):
            zy-=dy[1]
            zx-=dx[1]
            if zx==x and zy==y:
                break
            if vis[zy][zx]==(y, x): #시작위치가 내것이라면
                cnt+=1
                vis[zy][zx]=0
                
import sys
input=sys.stdin.readline
N,M=map(int, input().strip().split())
board=[list(map(int, input().strip().split())) for i in range(N)]
vis=[[0 for i in range(M)] for j in range(N)]
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
arr=[]
cctv=[]
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append([i,j])
        elif board[i][j] == 0:
            cnt+=1
backtracking(0)
print(min(arr))