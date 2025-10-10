from collections import deque
from collections import defaultdict
def solution(board):
    lenn=len(board)
    new_board=[[defaultdict(int) for i in range(lenn)] for j in range(lenn)]
    answer = 0
    dsmb=['U','R','D','L']#위, 오른, 아래, 왼
    dy=[-1, 0, 1, 0]
    dx=[0, 1, 0, -1]
    dq=deque([[-1,0,0]])
    while dq:
        tmp=dq.popleft()
        for i in range(4):
            y=dy[i]+tmp[1]
            x=dx[i]+tmp[2]
            if y<0 or x<0 or lenn<=y or lenn<=x or board[y][x]==1:
                continue
            if tmp[0]==-1:
                new_board[y][x][f'{i}']=100
                dq.append([i,y,x])
            else:
                now=0
                if tmp[0]!=i:
                    now=new_board[tmp[1]][tmp[2]][f'{tmp[0]}']+600
                elif tmp[0]==i:
                    now=new_board[tmp[1]][tmp[2]][f'{i}']+100
                    
                    
                if f'{i}' not in new_board[y][x].keys() or (new_board[y][x][f'{i}']!=0 and now<new_board[y][x][f'{i}']):
                    new_board[y][x][f'{i}']=now
                    dq.append([i,y,x])
    answer=min(new_board[lenn-1][lenn-1].values())
    return answer