import sys
input=sys.stdin.readline
N=int(input().strip())
li=set()
for _ in range(N):
    li.add(int(input().strip()))
li=tuple(li)
li=sorted(li)
for i in range(N-1, -1,-1):
    print(li[i])