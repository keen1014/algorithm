import sys
input=sys.stdin.readline
N=int(input().strip())
li={}
for _ in range(-1000000,1000001):
    li[_]=0
for _ in range(N):
    li[int(input().strip())]+=1
for i in range(-1000000,1000001):
    while 0<li[i]:
        li[i]-=1
        print(i)