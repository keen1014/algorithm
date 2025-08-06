def rotation(r, c, list):
    rtboard=[[0 for i in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            rtboard[j][r-1-i]=list[i][j]
    return c, r, rtboard

def symmetry(r, c, list):
    rtboard=[[0 for i in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            rtboard[i][j]=list[i][c-j-1]
    return r, c, rtboard
import sys
input=sys.stdin.readline
N, M = map(int, input().strip().split())
board=[list(map(int, input().strip().split())) for _ in range(N)]
answer=[]
tetromino=[[[1,1,1,1]], [[1,1],[1,1]], [[1,0],[1,0],[1,1]], [[1,0],[1,1],[0,1]], [[1,1,1],[0,1,0]]]
for i in range(5):
    st=tetromino[i]
    for _ in range(4):
        c, r, st=rotation(len(st), len(st[0]), st)
        # print(*st, sep='\n')
        poliomino=[]
        for k in range(c):
            for z in range(r):
                if st[k][z]==1:
                    poliomino.append([k,z])
        for y in range(N):
            for x in range(M):
                sum=0
                if N<=y+c-1 or M<=x+r-1:
                    continue
                for pol in range(len(poliomino)):
                    ly,lx=poliomino[pol]
                    sum+=board[y+ly][x+lx]
                # print(y,x, sum)
                answer.append(sum)
                
        c,r,stt=symmetry(len(st), len(st[0]), st)
        # print('stt',*stt, sep='\n')
        poliomino=[]
        for k in range(c):
            for z in range(r):
                if stt[k][z]==1:
                    poliomino.append([k,z])
        for y in range(N):
            for x in range(M):
                sum=0
                if N<=y+c-1 or M<=x+r-1:
                    continue
                for pol in range(len(poliomino)):
                    ly,lx=poliomino[pol]
                    sum+=board[y+ly][x+lx]
                # print(y,x, sum)
                answer.append(sum)
    # print('\n')
print(max(answer))