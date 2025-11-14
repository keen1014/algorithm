def prepare_expression(expr):
        # 1. 숫자 뒤의 x (예: 2x -> 2*x)
        expr = re.sub(r'(\d)x', r'\1*x', expr)
        # 2. 숫자 뒤의 ( (예: 2(x+1) -> 2*(x+1))
        expr = re.sub(r'(\d)\(', r'\1*(', expr)
        # 3. ) 뒤의 ( (예: (x+1)(x+2) -> (x+1)*(x+2))
        expr = re.sub(r'\)\(', r')*(', expr)
        # 4. ) 뒤의 x (예: (x+1)x -> (x+1)*x)
        expr = re.sub(r'\)x', r')*x', expr)
        # 5. x 뒤의 ( (예: x(x+1) -> x*(x+1))
        expr = re.sub(r'x\(', r'x*(', expr)
        # 6. ) 뒤의 숫자 (예: (x+1)2 -> (x+1)*2)
        expr = re.sub(r'\)(\d)', r')*\1', expr)
        # 7. x 뒤의 숫자 (예: x2 -> x*2)
        #    (이건 'x**2' (제곱)과 충돌할 수 있어 조심해야 하지만,
        #     제곱을 **로 쓴다는 가정 하에 추가)
        # expr = re.sub(r'x(\d)', r'x*\1', expr)
        return expr
class Solution:
    def solveEquation(self, equation: str) -> str:
        a,b=equation.split('=')
        a=prepare_expression(a)
        b=prepare_expression(b)
        val=-1
        cnt=0
        for i in range(-1000,1001):
            if eval(a.replace('x', f'({i})')) == eval(b.replace('x', f'({i})')):
                val=i
                cnt+=1
        if cnt>1:
            return "Infinite solutions"
        elif cnt==0:
            return "No solution"
        return f"x={val}"
