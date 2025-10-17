import sys
input=sys.stdin.readline
n = int(input().strip())
li=[]
for i in range(n):
    li.append(list(map(int, input().strip().split())))
li=sorted(li, key=lambda x: (x[1], x[0]))
front=li[0][0]
back=li[0][1]
cnt=1
for i in range(1,n):
    if li[i][0]<back:
        continue
    front=li[i][0]
    back=li[i][1]
    cnt+=1
print(cnt)