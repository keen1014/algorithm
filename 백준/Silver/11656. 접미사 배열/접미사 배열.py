import sys
input=sys.stdin.readline
li=input().strip().split()
lilen=len(li[0])
suffix=[]
for i in range(lilen):
    suffix.append(li[0][i:])
print(*sorted(suffix), sep='\n')