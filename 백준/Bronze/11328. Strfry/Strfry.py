import sys
input = sys.stdin.readline
A = int(input())
answer=[]
for i in range(A):
    B= list(map(str, input().split()))
    num=[0]*26
    num2=[0]*26
    for i in B[0]:
        num[ord(i)-97]+=1
        
    for i in B[1]:
        num2[ord(i)-97]+=1
    if num == num2:
        answer.append("Possible")
    else:
        answer.append("Impossible")
print(*answer, sep='\n')