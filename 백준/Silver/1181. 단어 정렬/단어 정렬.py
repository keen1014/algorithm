import sys
input=sys.stdin.readline
N=int(input().strip())
li=set()
for _ in range(N):
    li.add(input().strip())
li=sorted(li)
print(*sorted(li, key=lambda x: len(x)), sep='\n')