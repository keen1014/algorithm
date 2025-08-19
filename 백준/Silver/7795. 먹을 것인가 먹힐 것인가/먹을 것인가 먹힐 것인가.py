import sys
input=sys.stdin.readline
N=int(input().strip())
li=[]
for _ in range(N):
    A, B=input().strip().split()
    ans=0
    answer=[]
    Ali=list(map(int, input().strip().split()))
    Bli=list(map(int, input().strip().split()))
    Ali.sort()
    Bli.sort()
    for i in Ali:
        for j in range(ans,len(Bli)):
            if Bli[j]<i:
                ans+=1
            else:
                break
        answer.append(ans)
    print(sum(answer))