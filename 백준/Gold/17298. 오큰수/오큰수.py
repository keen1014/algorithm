import sys
input = sys.stdin.readline
n=int(input().strip())
h=list(map(int, input().strip().split()))
s=[]
a=[-1]*n
m=0
for i in range(n):
    tmp=h.pop()
    while s and tmp>=s[-1]:
        s.pop()
    if not s:
        a[n-i-1]=-1
    else:
        a[n-i-1]=s[-1]
    s.append(tmp)
print(*a)