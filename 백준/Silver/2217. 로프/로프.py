import sys
input=sys.stdin.readline
n = int(input().strip())
li=[]
for i in range(n):
    li.append(int(input().strip()))
li.sort()
tmp=0
for i in range(n):
    if tmp<li[i]*(n-i):
        tmp=li[i]*(n-i)
print(tmp)