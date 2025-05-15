import sys
input=sys.stdin.readline

n = int(input().strip())
a=[]
star=[]
tmp=0
cnt=0
while 1:
    if cnt == n:
        print(*star, sep='\n')
        break
    k = int(input().strip())
    if tmp <= k:
        for i in range(tmp, k):
            a.append(i+1)
            star.append('+')
        a.pop()
        star.append('-')
        cnt+=1
        tmp =k
    elif a[len(a)-1] == k:
        a.pop()
        star.append('-')
        cnt+=1
    else:
        print("NO")
        break