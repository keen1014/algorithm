import sys
input=sys.stdin.readline
N=int(input().strip())
d=[[0,0,0] for i in range(N+1)]
R,G,B=list(map(int, input().strip().split()))
d[1][0]=R
d[1][1]=G
d[1][2]=B
for i in range(2, N+1):
    R,G,B=list(map(int, input().strip().split()))
    d[i][0]=R+min(d[i-1][1], d[i-1][2])
    d[i][1]=G+min(d[i-1][0], d[i-1][2])
    d[i][2]=B+min(d[i-1][0], d[i-1][1])
print(min(d[N]))