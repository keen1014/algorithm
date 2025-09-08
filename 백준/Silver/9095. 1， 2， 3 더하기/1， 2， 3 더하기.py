import sys
input=sys.stdin.readline
T=int(input().strip())
d=[0]*12
d[1]=1
d[2]=2
d[3]=4
d[4]=d[1]+d[2]+d[3]
d[5]=d[2]+d[3]+d[4]
d[6]=d[3]+d[4]+d[5]
d[7]=d[4]+d[5]+d[6]
d[8]=d[5]+d[6]+d[7]
d[9]=d[6]+d[7]+d[8]
d[10]=d[7]+d[8]+d[9]
d[11]=d[8]+d[9]+d[10]
for i in range(T):
    n=int(input().strip())
    print(d[n])