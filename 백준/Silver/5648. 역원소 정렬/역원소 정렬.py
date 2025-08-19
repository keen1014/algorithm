import sys
input=sys.stdin.readline
N=list(input().strip().split())
li=N[-1:0:-1]
tmp=[]
tmp2=[]
for i in li:
    tmp.append(int(i[::-1]))
    
while len(tmp)!=int(N[0]):
    tmp2=list(input().strip().split())
    for j in tmp2:
        tmp.append(int(j[::-1]))

tmp.sort()
print(*tmp, sep='\n')