import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
for i in range(N):
    li.append(list(map(int, input().strip().split())))
li=sorted(li)
for i in range(N):
    print(*li[i])