import sys
input=sys.stdin.readline
N=int(input().strip())
li={}
for _ in range(10001):
    li[_]=0
for _ in range(N):
    li[int(input().strip())]+=1
for _ in range(10001):
    while li[_]!=0:
        li[_]-=1
        print(_)