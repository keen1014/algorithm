def solution(board, moves):
    stack=[]
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1]==0:
                continue
            elif board[j][moves[i]-1]!=0:
                if stack and board[j][moves[i]-1]==stack[-1]:
                    stack.pop()
                    board[j][moves[i]-1]=0
                    answer+=2
                    break
                stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break
    return answer