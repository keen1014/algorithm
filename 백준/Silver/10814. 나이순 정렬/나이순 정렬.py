import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
li={}
for i in range(1, 201):
    li[i]=deque([])
for i in range(N):
    age, name=input().strip().split()
    li[int(age)].append(name)
for i in range(1, 201):
    while li[i]!=deque([]):
        print(i, li.get(i).popleft())