import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
for _ in range(N):
    li.append(input().strip().split())
    for i in range(1,4):
        li[_][i]=int(li[_][i])
li.sort()
li.sort(key=lambda x: (-x[1], x[2], -x[3]))
for i in range(N):
    print(li[i][0])