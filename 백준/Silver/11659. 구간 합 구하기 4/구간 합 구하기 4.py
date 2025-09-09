import sys
input=sys.stdin.readline
N, M=list(map(int, input().strip().split()))
li=list(map(int, input().strip().split()))
d=[0]*100001
d[1]=li[0]
for i in range(2,N+1):
    d[i]=d[i-1]+li[i-1]
for j in range(M):
    y,x=list(map(int, input().strip().split()))
    print(d[x]-d[y-1])