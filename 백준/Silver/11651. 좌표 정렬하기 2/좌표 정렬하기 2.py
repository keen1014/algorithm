import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
for i in range(N):
    li.append(list(map(int, input().strip().split())))
li.sort()
li.sort(key= lambda st: st[1])
for i in range(len(li)):
    print(*li[i])