import sys
input = sys.stdin.readline
s= list(input().strip())
n= int(input())
now=len(s)
b=[]
for i in range(n):
    cmd=list(input().split())
    if cmd[0] == 'B':
        if s:
            s.pop()
    elif cmd[0] == 'L':
        if s:
            b.append(s.pop())
    elif cmd[0] =='D':
        if b:
            s.append(b.pop())
    elif cmd[0] =='P':
        s.append(cmd[1])
print("".join(s+b[::-1]))