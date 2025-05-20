from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()
n=int(input())
stack=deque([])
for i in range(n):
    stack.append(i+1)
while len(stack)!=1:
    stack.popleft()
    stack.append(stack.popleft())
print(stack.pop())