def backtracking(n):
    if n==sum(operator):
        global MAX, MIN
        ans=A[0]
        for j in range(n):
            if li[j]==0:
                ans+=A[j+1]
            elif li[j]==1:
                ans-=A[j+1]
            elif li[j]==2:
                ans*=A[j+1]
            elif li[j]==3:
                if ans==0:
                    ans=0
                elif ans<0:
                    ans=-(abs(ans)//A[j+1])
                else:
                    ans//=A[j+1]
        answer.append(ans)
        return
    for i in range(len(op)):
        if vis[i]==False:
            if n==0 and op[i] in visl:
                continue
            if n==0:
                visl.append(op[i])
            vis[i]=True
            li[n]=op[i]
            backtracking(n+1)
            vis[i]=False



# def backtrackingnum(n):
#     global MAX, MIN
#     if n==N:
#         ans=nli[0]
#         for j in range(N-1):
#             if li[j]==0:
#                 ans+=nli[j+1]
#             elif li[j]==1:
#                 ans-=nli[j+1]
#             elif li[j]==2:
#                 ans*=nli[j+1]
#             elif li[j]==3:
#                 if ans==0:
#                     ans=0
#                 elif ans<0:
#                     ans=-(abs(ans)//nli[j+1])
#                 else:
#                     ans//=nli[j+1]

#         if MAX<ans:
#             print(nli)
#             print(li)
#             print(ans)
#             MAX=ans
#         if ans<MIN:
#             MIN=ans
#         return
#     for i in range(len(A)):
#         if nvis[i]==False:
#             nvis[i]=True
#             nli[n]=A[i]
#             backtrackingnum(n+1)
#             nvis[i]=False
import sys
input=sys.stdin.readline
N=int(input().strip())
A=list(map(int, input().strip().split()))
operator=list(map(int, input().strip().split()))
op=[]
li=[0]*sum(operator)
vis=[False]*sum(operator)
visl=[]

nvis=[False]*len(A)
nli=[0]*len(A)
answer=[]
MIN=0
MAX=0
for i in range(len(operator)):
    for _ in range(operator[i]):
        op.append(i)
backtracking(0)
print(max(answer))
print(min(answer))