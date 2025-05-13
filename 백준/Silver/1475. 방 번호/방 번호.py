s = input()
arr = [0] * 10
for i in s:
    arr[ord(i) - ord('0')-1]+=1
if max(arr) == arr[5] or max(arr) == arr[8]:
    tmp=int((arr[5]+arr[8])/2+(arr[5]+arr[8])%2)
    arr[5]=0
    arr[8]=0
    if max(arr)<=tmp:
        print(tmp)
    else:
        print(max(arr))
else:
    print(max(arr))