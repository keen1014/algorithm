import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
     li.append(list(map(int, input().split())))
li.sort(key=lambda x: -x[1])
answer=1000001
for t, s in li:
    answer=min(answer, s)
    answer-=t
if answer>0:
    print(answer)
else:
    print(-1)