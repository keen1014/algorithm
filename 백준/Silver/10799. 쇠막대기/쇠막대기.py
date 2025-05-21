import sys
input = sys.stdin.readline
n=input().strip()
stack=[]
n=n.split('()')
n=" ".join(n)
cnt=0
for i in n:
    if i=='(':
        stack.append(i)
    elif i == ')':
        stack.pop()
        cnt+=1
    elif i == ' ':
        cnt+=len(stack)
print(cnt)