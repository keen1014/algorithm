import sys
input = sys.stdin.readline
n=int(input().strip())
h=[]
stack=[]
a=[0]*n
for i in range(n):
    h.append(int(input()))

    
for i in range(n):
    tmp=h.pop()
    cnt=0
    while stack and tmp>stack[-1][1]:
        cnt=cnt+1+a[stack.pop()[0]]
    stack.append([n-i-1,tmp])
    a[n-i-1]=cnt
print(sum(a))