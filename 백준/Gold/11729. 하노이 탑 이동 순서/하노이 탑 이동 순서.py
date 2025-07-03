def hanoi(a, b, N):
    if N==1:
        return print(a, b)
    hanoi(a, 6-a-b, N-1)
    print(a, b)
    hanoi(6-a-b, b, N-1)
import sys
input=sys.stdin.readline
N=int(input().strip())
print((1<<N)-1)
hanoi(1,3,N)