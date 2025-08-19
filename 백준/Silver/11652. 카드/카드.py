import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
dic={}
for i in range(N):
    li.append(int(input().strip()))
setli=set(li)
for i in setli:
    dic[i]=0
while li:
    dic[li.pop()]+=1
M=0
for i in dic.keys():
    li.append([dic[i],i])
    if M<dic[i]:
        M=dic[i]
ans=[]
for i in li:
    if i[0]==M:
        ans.append(i[1])
ans.sort()

print(ans[0])
