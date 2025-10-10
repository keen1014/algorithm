from collections import deque
def solution(places):
    
    def BFS(dq, board):
        dx=[0, 1, 0, -1]
        dy=[-1, 0, 1, 0]
        
        
        while dq:
            tmpdq=deque([])
            tmp=dq.popleft()
            tmpdq.append(tmp)
            new_board=[[0 for i in range(5)] for j in range(5)]
            new_board[tmp[1]][tmp[2]]=-1
            while tmpdq:
                yx=tmpdq.popleft()
                for i in range(4):
                    cnt=yx[0]
                    ly=yx[1]+dy[i]
                    lx=yx[2]+dx[i]
                    if ly<0 or lx<0 or 4<ly or 4<lx or board[ly][lx]=='X' or new_board[ly][lx]!=0:
                        continue
                    if board[ly][lx]=='P':
                        return 0
                    if 1<cnt:
                        tmpdq.append([cnt-1, ly, lx])
                    else:
                        continue
        else:
            return 1
                
            
    answer = []        
    for i in range(5):
        q=deque([])
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=='P':
                    q.append([2,j,k])
                       
        answer.append(BFS(q, places[i]))
    
    
    return answer