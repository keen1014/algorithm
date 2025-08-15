import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
for _ in range(N):
    li.append(int(input().strip()))
print(*sorted(li), sep='\n')