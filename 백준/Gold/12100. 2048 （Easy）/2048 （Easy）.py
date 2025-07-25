def backtracking(n):
    global bignum
    if n==6:
        if bignum<max(map(max, cp_board[5])):
            bignum=max(map(max, cp_board[5]))
        return
    for i in range(4):
        li[n-1]=i
        move(i,n) #방향, 몇번째
        backtracking(n+1)
        for x in range(N):
            for y in range(N):
                cp_board[n][x][y] = 0
def move(dsnb, k):
    for i in range(N):
        for j in range(N):
            cp_board[k][i][j]=cp_board[k-1][i][j]
    if dsnb==0:
        for i in range(N): #한줄씩 가져오기
            l=deque([cp_board[k-1][j][i] for j in range(N) if cp_board[k-1][j][i]!=0])
            #0이 아닌 정수 리스트 저장
            newl=[]
            while l: #앞에서 부터 같으면 더해서 다시 리스트에 추가, 다르면 그냥 추가
                if 2<=len(l) and l[0]==l[1]:
                    newl.append(l[0]*2)
                    l.popleft()
                    l.popleft()
                else:
                    newl.append(l.popleft())
            for s in range(N):
                if s<len(newl):
                    cp_board[k][s][i]=newl[s]
                else:
                    cp_board[k][s][i]=0
    elif dsnb==1:
        for i in range(N): #한줄씩 가져오기
            l=deque([cp_board[k-1][i][j] for j in range(N) if cp_board[k-1][i][j]!=0])
            #0이 아닌 정수 리스트 저장
            newl=[]
            while l: #앞에서 부터 같으면 더해서 다시 리스트에 추가, 다르면 그냥 추가
                if 2<=len(l) and l[0]==l[1]:
                    newl.append(l[0]*2)
                    l.popleft()
                    l.popleft()
                else:
                    newl.append(l[0])
                    l.popleft()
            for s in range(N):
                if s<len(newl):
                    cp_board[k][i][s]=newl[s]
                else:
                    cp_board[k][i][s]=0
    elif dsnb==2:
        for i in range(N): #한줄씩 가져오기
            l=deque([cp_board[k-1][j][i] for j in range(N-1, -1, -1) if cp_board[k-1][j][i]!=0])
            #0이 아닌 정수 리스트 저장
            newl=[]
            while l: #앞에서 부터 같으면 더해서 다시 리스트에 추가, 다르면 그냥 추가
                if 2<=len(l) and l[0]==l[1]:
                    newl.append(l[0]*2)
                    l.popleft()
                    l.popleft()
                else:
                    newl.append(l[0])
                    l.popleft()
            for s in range(N):
                pos=N-1-s
                if s<len(newl):
                    cp_board[k][pos][i]=newl[s]
                else:
                    cp_board[k][pos][i]=0
    elif dsnb==3:
        for i in range(N): #한줄씩 가져오기
            l=deque([cp_board[k-1][i][j] for j in range(N-1, -1, -1) if cp_board[k-1][i][j]!=0])
            #0이 아닌 정수 리스트 저장
            newl=deque([])
            while l: #앞에서 부터 같으면 더해서 다시 리스트에 추가, 다르면 그냥 추가
                if 2<=len(l) and l[0]==l[1]:
                    newl.append(l[0]*2)
                    l.popleft()
                    l.popleft()
                else:
                    newl.append(l[0])
                    l.popleft()
            for s in range(N):
                pos=N-1-s
                if s<len(newl):
                    cp_board[k][i][pos]=newl[s]
                else:
                    cp_board[k][i][pos]=0
import sys
from collections import deque
input=sys.stdin.readline
bignum=0
dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
N=int(input().strip())
cp_board=[[[0 for i in range(N)] for j in range(N)] for k in range(6)]
cp_board[0]=[list(map(int, input().strip().split())) for _ in range(N)]
li=[0]*5
#uldr 4방향을 모두 돌면서 5번 움직여야함 결국 모든 조합을 돌아서 가장 큰 값을
#찾아보아야 나오는 문제
backtracking(1)
print(bignum)