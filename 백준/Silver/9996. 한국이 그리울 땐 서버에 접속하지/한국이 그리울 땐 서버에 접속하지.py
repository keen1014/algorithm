import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
pattern=input().strip()
pattern=pattern.split('*')
for i in range(N):
    s=input().strip()
    s=s.replace(pattern[0], ' ')
    s=s.replace(pattern[1], ' ')
    if s[0]==' 'and s[-1] == ' ':
        print('DA')
    else:
        print('NE')