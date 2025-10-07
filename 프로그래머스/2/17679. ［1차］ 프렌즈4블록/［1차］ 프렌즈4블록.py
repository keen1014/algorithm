from collections import deque
def solution(m, n, board):
    li=set()
    answer = 0
    for i in range(m):
        board[i]=list(board[i])
        
        
    def BFS():
        deleteboard=[[0 for i in range(n)] for j in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!=0:
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        li.add((i,j))
                        li.add((i,j+1))
                        li.add((i+1,j))
                        li.add((i+1,j+1))
                        deleteboard[i][j]=1
                        deleteboard[i][j+1]=1
                        deleteboard[i+1][j]=1
                        deleteboard[i+1][j+1]=1
        
    def sorrt():
        tmpboard=[[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            tmpli=[]
            for j in range(m-1,-1,-1):
                if board[j][i]!=0:
                    tmpli.append(board[j][i])
            for k in range(m-len(tmpli)):
                tmpli.append(0)
            for z in range(m):
                board[z][i]=tmpli[m-1-z]
    while True:        
        BFS()
        if len(li)==0:
            break
        answer+=len(li)
        while li:
            ly, lx=li.pop()
            board[ly][lx]=0
        sorrt()
    return answer