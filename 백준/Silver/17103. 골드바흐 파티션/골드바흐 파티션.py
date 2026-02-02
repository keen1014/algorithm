import sys
input=sys.stdin.readline
T=int(input())
sosu=[True]*1000001
sosu[0]=sosu[1]=False
for i in range(2, int(1000000**0.5)):
    if sosu[i]:
        for j in range(i*i, 1000000+1, i):
            sosu[j]=False
# print(sosu)
this_prime=[i for i, prime in enumerate(sosu) if prime]

for _ in range(T):
    N=int(input())
    vis=[False]*(N+1)
    answer=0
    for y in this_prime:
        if y>N//2:
            break
        if vis[y]:
            continue
        if sosu[N-y]:
            vis[N-y]=True
            answer+=1
    print(answer)