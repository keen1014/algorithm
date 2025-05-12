a=int(input())
arr=list(map(int, input().split()))
target=int(input())
summery=0
for s in arr:
    if target==s:
        summery+=1
print(summery)