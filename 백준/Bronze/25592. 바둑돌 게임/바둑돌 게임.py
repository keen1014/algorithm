import sys
input=sys.stdin.readline
N=int(input().strip())
for i in range(1, N+1):
    N-=i
    if i%2==0 and N<0:
        print(0)
        break
    if i%2 and N<=0:
        print(abs(N))
        break