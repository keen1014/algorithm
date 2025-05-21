import sys
input = sys.stdin.readline
tmp=''
s=[]
while True:
    tmp = input().rstrip()
    if tmp=='.':
        break
    else:
        s.append(tmp)
for i in range(len(s)):
    j = 0
    e=[]
    while s[i][j]!='.':
        if s[i][j]=='(':
            e.append(s[i][j])
        elif s[i][j]=='[':
            e.append(s[i][j])
        elif s[i][j]== ']':
            if e and e[-1] == '[':
                e.pop()
            else:
                print('no')
                break
        elif s[i][j]==')':
            if e and e[-1] == '(':
                e.pop()
            else:
                print('no')
                break
        j+=1
    else:
        if e:
            print('no')
        else:
            print('yes')