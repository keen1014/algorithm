import sys
import math
input = sys.stdin.readline
N, K= map(int, input().split())
m=[0]*6
f=[0]*6
count=0
for i in range(N):
    st=list(map(int, input().split()))
    if st[0]==1:
        m[st[1]-1]+=1
    else:
        f[st[1]-1]+=1
for i in range(6):
    count+=((m[i]+K-1)//K)
    count+=((f[i]+K-1)//K)
print(int(count))