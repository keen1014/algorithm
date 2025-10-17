import sys
input=sys.stdin.readline
n, k = map(int, input().strip().split())
coin=[]
cnt=0
for i in range(n):
    coin.append(int(input().strip()))
coin=sorted(coin, reverse=True)
for j in range(n):
    if coin[j]> k:
        continue
    c, k=divmod(k, coin[j])
    cnt+=c
print(cnt)