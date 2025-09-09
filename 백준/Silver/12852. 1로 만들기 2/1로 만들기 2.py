import sys
input=sys.stdin.readline
x=int(input().strip())
d=[[0,0] for _ in range(x+1)]
d[1]=[0,1]
for i in range(2,x+1):
    d[i]=[d[i-1][0]+1, i-1]
    if i%3==0:
        if min(d[i][0], d[i//3][0]+1) == (d[i//3][0]+1):
            d[i]=[d[i//3][0]+1, i//3]
    if i%2==0:
        if min(d[i][0], d[i//2][0]+1) == (d[i//2][0]+1):
            d[i]=[d[i//2][0]+1, i//2]
print(d[x][0])
print(x, end=' ')
while x!=1:
    print(d[x][1], end=' ')
    x=d[x][1]