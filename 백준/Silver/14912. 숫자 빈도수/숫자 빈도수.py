import sys
input=sys.stdin.readline
dic={}
for i in range(10):
    dic[i]=0
n, d=map(int, input().split())
for i in range(1, n+1):
    while i:
        dic[i%10]+=1
        i//=10
print(dic[d])