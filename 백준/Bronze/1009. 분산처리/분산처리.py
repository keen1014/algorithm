import sys
input=sys.stdin.readline
N=int(input().strip())
A=[[10, 10, 10, 10], [1, 1, 1, 1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6],[5, 5, 5, 5],[6, 6, 6, 6],[7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1]]
for _ in range(N):
    a, b=list(map(int, input().split()))
    aa=a%10
    bb=b%4
    print(A[aa][bb-1])