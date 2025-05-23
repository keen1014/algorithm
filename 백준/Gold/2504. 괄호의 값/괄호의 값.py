import sys
input = sys.stdin.readline

n = input().strip()
stack = []

# 괄호 쌍을 숫자로 대체
n = n.replace('()', '2')
n = n.replace('[]', '3')

for ch in n:
    if ch == '(' or ch == '[':
        stack.append(ch)
    elif ch == '2' or ch == '3':
        stack.append(int(ch))
    elif ch == ')':
        tmp = 0
        while stack and isinstance(stack[-1], int):
            tmp += stack.pop()
        if not stack or stack[-1] != '(':
            print(0)
            break
        stack.pop()  # '(' 제거
        stack.append(tmp * 2)
    elif ch == ']':
        tmp = 0
        while stack and isinstance(stack[-1], int):
            tmp += stack.pop()
        if not stack or stack[-1] != '[':
            print(0)
            break
        stack.pop()  # '[' 제거
        stack.append(tmp * 3)
else:
    # 남은 스택에 숫자 외에 문자열이 있다면 잘못된 구조
    if all(isinstance(i, int) for i in stack):
        print(sum(stack))
    else:
        print(0)
