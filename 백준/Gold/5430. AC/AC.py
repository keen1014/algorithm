from collections import deque
import sys
input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    o=1
    dq=deque([])
    cmd=input().strip()
    num=int(input().strip())
    s = input().strip()
    s=s[1:-1].split(',')
    for j in range(num):
        dq.append(s[j])
    for e in range(len(cmd)):
        if cmd[e] == 'R':
            if o==1:
                o=-1
            else:
                o=1
        elif cmd[e] == 'D':
            if dq and o==1:
                dq.popleft()
            elif dq and o==-1:
                dq.pop()
            elif not dq:
                print('error')
                break
    else:
        if o==1:
            print(f"[{','.join(dq)}]")
        elif o==-1:
            print(f"[{','.join(reversed(dq))}]")