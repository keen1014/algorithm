def rotation(r, c, list):
    rtboard=[[0 for i in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            rtboard[j][r-1-i]=list[i][j]
    return rtboard
import sys
input=sys.stdin.readline
N=int(input().strip())
for i in range(N):
    
    board=[[['w','w','w'],['w','w','w'],['w','w','w']],[['y','y','y'],['y','y','y'],['y','y','y']],[['r','r','r'], ['r','r','r'], ['r','r','r']],[['o','o','o'], ['o','o','o'], ['o','o','o']],[['g','g','g'], ['g','g','g'], ['g','g','g']],[['b','b','b'], ['b','b','b'], ['b','b','b']]]

    n=int(input().strip())
    tmp=list(input().strip().split())

    for i in tmp:
        if i[0]=='U':
            if i[1]=='+':
                board[0]=rotation(3,3,board[0])
                tm=[board[3][0][0], board[3][0][1], board[3][0][2]]
                board[3][0][0]=board[4][0][0]
                board[3][0][1]=board[4][0][1]
                board[3][0][2]=board[4][0][2]

                board[4][0][0]=board[2][0][0]
                board[4][0][1]=board[2][0][1]
                board[4][0][2]=board[2][0][2]
                
                board[2][0][0]=board[5][0][0]
                board[2][0][1]=board[5][0][1]
                board[2][0][2]=board[5][0][2]
                
                board[5][0][0]=tm[0]
                board[5][0][1]=tm[1]
                board[5][0][2]=tm[2]

            elif i[1]=='-':
                board[0]=rotation(3,3,board[0])
                board[0]=rotation(3,3,board[0])
                board[0]=rotation(3,3,board[0])
                tm=[board[3][0][0], board[3][0][1], board[3][0][2]]
                board[3][0][0]=board[5][0][0]
                board[3][0][1]=board[5][0][1]
                board[3][0][2]=board[5][0][2]

                board[5][0][0]=board[2][0][0]
                board[5][0][1]=board[2][0][1]
                board[5][0][2]=board[2][0][2]
                
                board[2][0][0]=board[4][0][0]
                board[2][0][1]=board[4][0][1]
                board[2][0][2]=board[4][0][2]
                
                board[4][0][0]=tm[0]
                board[4][0][1]=tm[1]
                board[4][0][2]=tm[2]

        elif i[0]=='D':
            if i[1]=='+':
                board[1]=rotation(3,3,board[1])
                tm=[board[3][2][0], board[3][2][1], board[3][2][2]]
                board[3][2][0]=board[5][2][0]
                board[3][2][1]=board[5][2][1]
                board[3][2][2]=board[5][2][2]

                board[5][2][0]=board[2][2][0]
                board[5][2][1]=board[2][2][1]
                board[5][2][2]=board[2][2][2]
                
                board[2][2][0]=board[4][2][0]
                board[2][2][1]=board[4][2][1]
                board[2][2][2]=board[4][2][2]
                
                board[4][2][0]=tm[0]
                board[4][2][1]=tm[1]
                board[4][2][2]=tm[2]

            elif i[1]=='-':
                board[1]=rotation(3,3,board[1])
                board[1]=rotation(3,3,board[1])
                board[1]=rotation(3,3,board[1])
                tm=[board[3][2][0], board[3][2][1], board[3][2][2]]
                board[3][2][0]=board[4][2][0]
                board[3][2][1]=board[4][2][1]
                board[3][2][2]=board[4][2][2]

                board[4][2][0]=board[2][2][0]
                board[4][2][1]=board[2][2][1]
                board[4][2][2]=board[2][2][2]
                
                board[2][2][0]=board[5][2][0]
                board[2][2][1]=board[5][2][1]
                board[2][2][2]=board[5][2][2]
                
                board[5][2][0]=tm[0]
                board[5][2][1]=tm[1]
                board[5][2][2]=tm[2]

                
            
        elif i[0]=='F':
            if i[1]=='+':
                board[2]=rotation(3,3,board[2])
                tm=[board[0][2][0], board[0][2][1], board[0][2][2]]
                board[0][2][0]=board[4][2][2]
                board[0][2][1]=board[4][1][2]
                board[0][2][2]=board[4][0][2]

                board[4][0][2]=board[1][0][0]
                board[4][1][2]=board[1][0][1]
                board[4][2][2]=board[1][0][2]
                
                board[1][0][2]=board[5][0][0]
                board[1][0][1]=board[5][1][0]
                board[1][0][0]=board[5][2][0]
                
                board[5][0][0]=tm[0]
                board[5][1][0]=tm[1]
                board[5][2][0]=tm[2]

            elif i[1]=='-':
                board[2]=rotation(3,3,board[2])
                board[2]=rotation(3,3,board[2])
                board[2]=rotation(3,3,board[2])
                tm=[board[0][2][0], board[0][2][1], board[0][2][2]]
                board[0][2][0]=board[5][0][0]
                board[0][2][1]=board[5][1][0]
                board[0][2][2]=board[5][2][0]

                board[5][0][0]=board[1][0][2]
                board[5][1][0]=board[1][0][1]
                board[5][2][0]=board[1][0][0]
                
                board[1][0][0]=board[4][0][2]
                board[1][0][1]=board[4][1][2]
                board[1][0][2]=board[4][2][2]
                
                board[4][0][2]=tm[2]
                board[4][1][2]=tm[1]
                board[4][2][2]=tm[0]
                
        elif i[0]=='B':
            
             # 0: U, 1: D, 2:F, 3:B, 4:L, 5:R
            if i[1]=='+':
                board[3]=rotation(3,3,board[3])
                tm=[board[0][0][0], board[0][0][1], board[0][0][2]]
                board[0][0][0]=board[5][0][2]
                board[0][0][1]=board[5][1][2]
                board[0][0][2]=board[5][2][2]

                board[5][0][2]=board[1][2][2]
                board[5][1][2]=board[1][2][1]
                board[5][2][2]=board[1][2][0]
                
                board[1][2][0]=board[4][0][0]
                board[1][2][1]=board[4][1][0]
                board[1][2][2]=board[4][2][0]
                
                board[4][0][0]=tm[2]
                board[4][1][0]=tm[1]
                board[4][2][0]=tm[0]

            elif i[1]=='-':
                board[3]=rotation(3,3,board[3])
                board[3]=rotation(3,3,board[3])
                board[3]=rotation(3,3,board[3])
                tm=[board[0][0][0], board[0][0][1], board[0][0][2]]
                board[0][0][0]=board[4][2][0]
                board[0][0][1]=board[4][1][0]
                board[0][0][2]=board[4][0][0]

                board[4][2][0]=board[1][2][2]
                board[4][1][0]=board[1][2][1]
                board[4][0][0]=board[1][2][0]
                
                board[1][2][2]=board[5][0][2]
                board[1][2][1]=board[5][1][2]
                board[1][2][0]=board[5][2][2]
                
                board[5][0][2]=tm[0]
                board[5][1][2]=tm[1]
                board[5][2][2]=tm[2]

                
                # =====================================================
        elif i[0]=='L':
            
            if i[1]=='+':
                board[4]=rotation(3,3,board[4])
                tm=[board[3][0][2], board[3][1][2], board[3][2][2]]
                board[3][0][2]=board[1][2][0]
                board[3][1][2]=board[1][1][0]
                board[3][2][2]=board[1][0][0]


                board[1][0][0]=board[2][0][0]
                board[1][1][0]=board[2][1][0]
                board[1][2][0]=board[2][2][0]
                
                board[2][0][0]=board[0][0][0]
                board[2][1][0]=board[0][1][0]
                board[2][2][0]=board[0][2][0]
                
                board[0][0][0]=tm[2]
                board[0][1][0]=tm[1]
                board[0][2][0]=tm[0]

            elif i[1]=='-':
                board[4]=rotation(3,3,board[4])
                board[4]=rotation(3,3,board[4])
                board[4]=rotation(3,3,board[4])
                tm=[board[3][0][2], board[3][1][2], board[3][2][2]]
                board[3][0][2]=board[0][2][0]
                board[3][1][2]=board[0][1][0]
                board[3][2][2]=board[0][0][0]
                
                board[0][0][0]=board[2][0][0]
                board[0][1][0]=board[2][1][0]
                board[0][2][0]=board[2][2][0]
                
                board[2][0][0]=board[1][0][0]
                board[2][1][0]=board[1][1][0]
                board[2][2][0]=board[1][2][0]

                board[1][2][0]=tm[0]
                board[1][1][0]=tm[1]
                board[1][0][0]=tm[2]
                
                
        elif i[0]=='R':
            #3:B , 0:U, 2:F, 1:D
            if i[1]=='+':
                board[5]=rotation(3,3,board[5])
                tm=[board[3][0][0], board[3][1][0], board[3][2][0]]
                board[3][0][0]=board[0][2][2]
                board[3][1][0]=board[0][1][2]
                board[3][2][0]=board[0][0][2]
                
                board[0][0][2]=board[2][0][2]
                board[0][1][2]=board[2][1][2]
                board[0][2][2]=board[2][2][2]
                
                board[2][0][2]=board[1][0][2]
                board[2][1][2]=board[1][1][2]
                board[2][2][2]=board[1][2][2]

                board[1][2][2]=tm[0]
                board[1][1][2]=tm[1]
                board[1][0][2]=tm[2]
            elif i[1]=='-':
                board[5]=rotation(3,3,board[5])
                board[5]=rotation(3,3,board[5])
                board[5]=rotation(3,3,board[5])
                tm=[board[3][0][0], board[3][1][0], board[3][2][0]]
                board[3][0][0]=board[1][2][2]
                board[3][1][0]=board[1][1][2]
                board[3][2][0]=board[1][0][2]
                
                board[1][0][2]=board[2][0][2]
                board[1][1][2]=board[2][1][2]
                board[1][2][2]=board[2][2][2]
                
                board[2][0][2]=board[0][0][2]
                board[2][1][2]=board[0][1][2]
                board[2][2][2]=board[0][2][2]

                board[0][2][2]=tm[0]
                board[0][1][2]=tm[1]
                board[0][0][2]=tm[2]
    for i in range(3):
        print(board[0][i][0],board[0][i][1],board[0][i][2], sep='')
    