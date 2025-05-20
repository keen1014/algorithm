import sys
input = sys.stdin.readline
n=int(input().strip())
h=[]
stack=[]
for i in range(n):
    p= list(input().strip().split())
    h.append(p)

    
for i in range(n):
    if h[i][0] == 'push':
        stack.append(h[i][1])
    elif h[i][0] == 'pop':
        if stack:
            print(stack.pop(0))
        else:
            print(-1)
    elif h[i][0] == 'size':
        print(len(stack))
    elif h[i][0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif h[i][0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif h[i][0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)