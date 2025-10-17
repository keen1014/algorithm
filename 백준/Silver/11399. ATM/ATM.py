import sys
input=sys.stdin.readline
n=int(input().strip())
li=list(map(int, input().strip().split()))
li=sorted(li)
answer=0
for i in range(n):
    answer+=li[i]*(n-i)
print(answer)