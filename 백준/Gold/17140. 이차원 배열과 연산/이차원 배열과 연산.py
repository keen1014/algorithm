import sys
input=sys.stdin.readline
r,c,k=list(map(int, input().strip().split()))
board=[list(map(int, input().strip().split())) for i in range(3)]
# print(*board, sep='\n')

for cnt in range(101):
    # if cnt==100:
    #     print(*board, sep='\n')
    #     print(len(board), len(board[0]))
    # print(cnt)
    if c<=len(board[0]) and r<=len(board):
        if board[r-1][c-1]==k:
            print(cnt)
            break
    if len(board[0])<=len(board):
        maxlen=0
        for z in range(len(board)):
            dict={}
            for j in set(board[z]):
                if j == 0:
                    continue
                dict[j]=0
            for i in range(len(board[z])):
                if board[z][i]==0:
                    continue
                dict[board[z][i]]+=1
            board[z]=[]
            for getdict in sorted(dict, key=lambda x: (dict.get(x), x)):
                board[z].append(getdict)
                board[z].append(dict[getdict])
            if 100<len(board[z]):
                board[z]=board[z][:100]
            if maxlen<len(board[z]):
                maxlen=len(board[z])
            for z in range(len(board)):
                while len(board[z])<maxlen:
                    board[z].append(0)
        # print(*board, sep='\n', end='\n\n')
    elif len(board)<len(board[0]):
        maxlen=0
        for iz in range(len(board[0])):
            dict={}
            li=[]
            for RL in range(len(board)):
                li.append(board[RL][iz])
            for j in set(li):
                if j == 0:
                    continue
                dict[j]=0
            for i in li:
                if i==0:
                    continue
                dict[i]+=1
            Rli=[]
            for getdict in sorted(dict, key=lambda x: (dict.get(x), x)):
                Rli.append(getdict)
                Rli.append(dict[getdict])
            while len(board)<len(Rli):
                board.append([0 for i in range(len(board[0]))])
            
            for w in range(len(board)):
                board[w][iz]=0
            for boardlen in range(len(Rli)):
                board[boardlen][iz]=Rli[boardlen]
            if maxlen<len(board):
                maxlen=len(board)
            # for z in range(len(board)):
            #     while len(board[z])<maxlen:
            #         board[z].append(0)
        
        while 100<len(board):
            board.pop()
        # print(*board, sep='\n', end='\n\n')
else:
    print(-1)