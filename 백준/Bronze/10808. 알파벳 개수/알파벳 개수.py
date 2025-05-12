s = list(input())
arr = [0] * 26
for i in s:
    arr[ord(i) - ord('a')]+=1
print(*arr)