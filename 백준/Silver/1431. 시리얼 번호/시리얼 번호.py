import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
a=0
for i in range(N):
    li.append(list(input().strip()))
li.sort()
for i in range(N):
    z=0
    for j in range(len(li[i])):
        if li[i][j]<'A':
            z+=int(li[i][j])
    li[i].append(z)
li.sort(key= lambda x: x[-1])
li.sort(key=lambda x: len(x))
for i in range(len(li)):
    print(*li[i][:-1], sep='')