import sys
input=sys.stdin.readline
D=[[0, 0, 0] for _ in range(301)]
T=int(input().strip())
li=[]
for i in range(T):
    li.append(int(input().strip()))
if T==1:
    print(li[0])
    exit()
D[1][1]=li[0]
D[2][1]=li[1]
D[2][2]=D[1][1]+li[1]

for i in range(3,T+1):
    D[i][1]=max(D[i-2][1], D[i-2][2])+li[i-1]
    D[i][2]=D[i-1][1]+li[i-1]
print(max(D[T][1],D[T][2]))