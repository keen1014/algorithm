import sys
from collections import deque
input=sys.stdin.readline
testcase=int(input().strip())
dx=[-1, -2, -2, -1, 1, 2, 2, 1]
dy=[-2, -1, 1, 2, 2, 1, -1, -2]
for i in range(testcase):
    dq=deque([])
    c=int(input().strip())
    cmap=[[0 for _ in range(c)]for w in range(c)]
    start=list(map(int, input().strip().split()))
    end=list(map(int, input().strip().split()))
    dq.append(start)
    while dq:
        tmp=dq.popleft()
        if tmp == end:
            print(cmap[tmp[0]][tmp[1]])
            break
        else:
            for k in range(8):
                x=dx[k]+tmp[0]
                y=dy[k]+tmp[1]
                if x<0 or y<0 or x>=c or y>=c or cmap[x][y]!=0:
                    continue
                else:
                    cmap[x][y]=cmap[tmp[0]][tmp[1]]+1
                    dq.append([x, y])