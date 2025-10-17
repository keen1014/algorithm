import sys
input=sys.stdin.readline
n=int(input().strip())
A=list(map(int, input().strip().split()))
B=list(map(int, input().strip().split()))
A=sorted(A)
K=sorted(B, reverse=True)
answer=0
for i in range(n):
    answer+=A[i]*K[i]
print(answer)