import sys
input=sys.stdin.readline
N, M=map(int, input().strip().split())
li=list(map(int, input().strip().split()))
tmp=set()
order=[]
dic={}
for i in li:
    if i not in tmp:
        tmp.add(i)
        order.append(i)
        dic[i]=1
    elif i in tmp:
        dic[i]+=1
order.sort(key=lambda x: dic[x], reverse=True)
ans=[]
for i in order:
    for j in range(dic[i]):
        ans.append(i)
print(*ans)